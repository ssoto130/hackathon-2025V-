from flask import Blueprint, jsonify
from lib.database_manager import db_manager
from lib import transformers
from lib.models import response_models as responses

question_set_bp = Blueprint('question_set', __name__)

@question_set_bp.route('/question-set/<question_set_id>', methods=['GET'])
def get_question_set_by_id(question_set_id):
    qs_db = db_manager.get_question_set(question_set_id)

    if not qs_db:
        return jsonify({"error": f"QuestionSet with ID '{question_set_id}' not found"}), 404
    
    qs_response = transformers.transform_question_set_db_to_response(qs_db)
    return jsonify(qs_response.model_dump())
