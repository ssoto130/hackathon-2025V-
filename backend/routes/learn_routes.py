from flask import Blueprint, jsonify
from lib.database_manager import db_manager
from lib import transformers
from lib.models import response_models as responses

learn_bp = Blueprint('learn', __name__)

@learn_bp.route('/learn/<learn_id>', methods=['GET'])
def get_learn_by_id(learn_id):
    learn_db = db_manager.get_learn(learn_id)

    if not learn_db:
        return jsonify({"error": f"Learn content with ID '{learn_id}' not found"}), 404
    
    learn_response = transformers.transform_learn_db_to_response(learn_db)
    return learn_response.model_dump_json()
