import json
import os
from app import create_app
from db import db
from lib.database_manager import db_manager
from lib.models.database_models import LearnDB, QuestionDB, QuestionSetDB, CourseDB, FileContentDB, TestCaseDB, HintDB

# Define the path for the JSON dump file
CONFIG_FOLDER = os.path.join(os.path.dirname(__file__), 'config')
JSON_DUMP_FILE = os.path.join(CONFIG_FOLDER, 'db_dump.json')

def load_db_from_json():
    """
    Loads content from a normalized JSON file and populates the database.
    """
    try:
        with open(JSON_DUMP_FILE, 'r') as f:
            all_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON dump file not found at {JSON_DUMP_FILE}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {JSON_DUMP_FILE}")
        return

    print(f"Loading data from {JSON_DUMP_FILE} into the database...")

    # Clear existing data for a clean load
    db.drop_all()
    db.create_all()
    print("Database cleared and re-initialized.")

    # Store mappings of old IDs to new IDs if ID generation is dynamic
    # For now, we assume IDs in JSON are the final IDs.

    # 1. Add Learn items
    print("Adding Learn items...")
    for learn_id, learn_data in all_data.get('learn', {}).items():
        learn_pdb = LearnDB(**learn_data)
        db_manager.add_learn(learn_pdb)
    print(f"Added {len(all_data.get('learn', {}))} Learn items.")

    # 2. Add FileContent, TestCase, Hint items (these are nested in Question)
    # We need to add them before questions if they are referenced by ID in questions
    # In our current Pydantic QuestionDB, they are embedded, so we'll handle them with Question.
    # However, if they were separate, this is where they'd go.
    # For now, we'll just ensure their IDs are present in the JSON.

    # 3. Add Question items
    print("Adding Question items...")
    for question_id, question_data in all_data.get('question', {}).items():
        # Reconstruct nested Pydantic models for files, hints, test_cases
        files_pdb = [FileContentDB(**f) for f in question_data.get('files', [])]
        hints_pdb = [HintDB(**h) for h in question_data.get('hints', [])]
        test_cases_pdb = [TestCaseDB(**tc) for tc in question_data.get('test_cases', [])]

        q_data_for_pdb = {k: v for k, v in question_data.items() if k not in ['files', 'hints', 'test_cases']}
        question_pdb = QuestionDB(**q_data_for_pdb, files=files_pdb, hints=hints_pdb, test_cases=test_cases_pdb)
        db_manager.add_question(question_pdb)
    print(f"Added {len(all_data.get('question', {}))} Question items.")

    # 4. Add QuestionSet items
    print("Adding QuestionSet items...")
    for qs_id, qs_data in all_data.get('question_set', {}).items():
        questions_in_set = []
        for q_ref_id in qs_data.get('questions', []):
            question_db = db_manager.get_question(q_ref_id)
            if question_db:
                questions_in_set.append(question_db)
            else:
                print(f"Warning: Question ID '{q_ref_id}' not found for QuestionSet '{qs_id}'. Skipping.")
        
        qs_pdb = QuestionSetDB(name=qs_data['name'], questions=questions_in_set)
        db_manager.add_question_set(qs_pdb)
    print(f"Added {len(all_data.get('question_set', {}))} QuestionSet items.")

    # 5. Add Course items
    print("Adding Course items...")
    for course_id, course_data in all_data.get('course', {}).items():
        question_sets_in_course = []
        for qs_ref_id in course_data.get('question_sets', []):
            qs_db = db_manager.get_question_set(qs_ref_id)
            if qs_db:
                question_sets_in_course.append(qs_db)
            else:
                print(f"Warning: QuestionSet ID '{qs_ref_id}' not found for Course '{course_id}'. Skipping.")
        
        course_pdb = CourseDB(name=course_data['name'], description=course_data['description'], question_sets=question_sets_in_course)
        db_manager.add_course(course_pdb)
    print(f"Added {len(all_data.get('course', {}))} Course items.")

    print("Database loading complete.")

if __name__ == '__main__':
    app = create_app()
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": os.getenv('DATABASE_URL'),
    })

    with app.app_context():
        load_db_from_json()
