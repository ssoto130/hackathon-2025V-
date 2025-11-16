import json
import os
from flask import Blueprint, jsonify
from lib.database_manager import db_manager
from lib.models import response_models as responses
from lib import transformers

base_content_bp = Blueprint('base_content', __name__)

# Load BASE_CONTENT_IDS from a configuration file
CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'default_content.json')

def load_base_content_ids():
    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {CONFIG_FILE_PATH} not found. Using empty default content IDs.")
        return {"courses": [], "learn": []}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {CONFIG_FILE_PATH}. Using empty default content IDs.")
        return {"courses": [], "learn": []}

@base_content_bp.route('/base-content', methods=['GET'])
def get_base_content():
    BASE_CONTENT_IDS = load_base_content_ids()

    content_for_set = []

    # fetch and transform courses
    for course_id in BASE_CONTENT_IDS.get("courses", []):
        course_db = db_manager.get_course(course_id)
        print(f"DEBUG: Fetched course_db for ID {course_id}: {course_db}") # DEBUG PRINT
        if course_db:
            course_response = transformers.transform_course_db_to_response(course_db)
            content_for_set.append(course_response)

    # fetch and transform learn items
    for learn_id in BASE_CONTENT_IDS.get("learn", []):
        learn_db = db_manager.get_learn(learn_id)
        if learn_db:
            learn_response = transformers.transform_learn_db_to_response(learn_db)
            content_for_set.append(learn_response)

    # create the final ContentSet response
    content_set = responses.ContentSet(
        type='contentSet',
        content=content_for_set
    )

    return jsonify(content_set.model_dump())
