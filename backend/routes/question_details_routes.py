from flask import Blueprint, jsonify
from lib.database_manager import db_manager
from lib import transformers
from lib.models import response_models as responses

question_details_bp = Blueprint('question_details', __name__)

@question_details_bp.route('/question-details/<question_id>', methods=['GET'])
def get_question_details_by_id(question_id):
    question_db = db_manager.get_question(question_id)

    if not question_db:
        return jsonify({"error": f"Question with ID '{question_id}' not found"}), 404
    
    learn_db = db_manager.get_learn(question_db.learn_id)
    if not learn_db:
        learn_response = responses.Learn(
            type='learn',
            learnId=question_db.learn_id,
            title='Unknown Learn Content',
            content='Learn content not found for this question.'
        )
    else:
        learn_response = transformers.transform_learn_db_to_response(learn_db)

    question_response = transformers.transform_question_db_to_full_response(question_db, learn_response)

    return jsonify(question_response.model_dump())
