from flask import Blueprint, request, jsonify
import requests
from test.mockDB import FAKE_DB

# TODO: add a queue system

PISTON_URL = "https://emkc.org/api/v2/piston/execute"

submit_bp = Blueprint("submit", __name__)

@submit_bp.route('/submit', methods=['POST'])
def post_submit_code():
    data = request.get_json()
    files = data.get('files', [])
    question_id = data.get('questionId')

    if not files:
        return {"message": "No files provided"}, 400

    if question_id not in FAKE_DB['questions']:
        return {"message": "Question not found"}, 404

    test_cases = FAKE_DB['questions'][question_id]['testCases']
    payload_files = [{"name": f["fileName"], "content": f["content"]} for f in files]

    testInput = ''
    result = ''
    expected_result = ''
    passed_tests = True
    for test_case in test_cases:
        testInput = test_case['input']
        expected_result = test_case['expectedOutput']

        payload = {
            "language": "java",
            "version": "*",
            "files": payload_files,
            "stdin": testInput,
            "args": []
        }

        try:
            res = requests.post(PISTON_URL, json=payload, timeout=10)
            res.raise_for_status()  
        except requests.Timeout:
            return {"message": "Execution timed out"}, 504
        except requests.HTTPError:
            return {"message": f"Piston API returned status {res.status_code}"}, 502
        except requests.RequestException as e:
            return {"message": f"Piston API request failed: {str(e)}"}, 502
        
        res_json = res.json()
        run = res_json.get("run", {})
        result = run.get("stdout", "")
        result += run.get("stderr", "")
        if result != expected_result:
            passed_tests = False
            break

    final_result = {
        'input': testInput,
        'result': result,
        'expectedResult': expected_result,
        'passedTests': passed_tests,
        'error': None
    }
    return jsonify(final_result)
