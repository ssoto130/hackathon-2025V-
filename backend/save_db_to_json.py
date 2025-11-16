import json
import os
from app import create_app
from db import db
from lib.database_manager import db_manager
from lib.models.SQLmodels import Learn as SQLLearn, Question as SQLQuestion, QuestionSet as SQLQuestionSet, Course as SQLCourse, FileContent as SQLFileContent, TestCase as SQLTestCase, Hint as SQLHint
from lib.models.database_models import LearnDB, QuestionDB, QuestionSetDB, CourseDB, FileContentDB, TestCaseDB, HintDB

# Define the path for the JSON dump file
CONFIG_FOLDER = os.path.join(os.path.dirname(__file__), 'config')
JSON_DUMP_FILE = os.path.join(CONFIG_FOLDER, 'db_dump.json')

def save_db_to_json():
    """
    Fetches all content from the database and saves it to a normalized JSON file.
    """
    all_data = {
        "learn": {},
        "question": {},
        "question_set": {},
        "course": {}
    }

    # Fetch all Learn items
    learn_items = db.session.query(SQLLearn).all()
    for item in learn_items:
        all_data["learn"][item.id] = LearnDB.model_validate(item).model_dump()

    # Fetch all Question items
    question_items = db.session.query(SQLQuestion).all()
    for item in question_items:
        # Hydrate full question including nested items
        question_db_model = db_manager._hydrate_question(item)
        
        # Embed nested objects directly
        question_dump = question_db_model.model_dump()
        question_dump['files'] = [FileContentDB.model_validate(f).model_dump() for f in item.files]
        question_dump['hints'] = [HintDB.model_validate(h).model_dump() for h in item.hints]
        question_dump['test_cases'] = [TestCaseDB.model_validate(tc).model_dump() for tc in item.test_cases]
        
        all_data["question"][item.id] = question_dump

    # Fetch all QuestionSet items
    qs_items = db.session.query(SQLQuestionSet).all()
    for item in qs_items:
        qs_db_model = db_manager._hydrate_question_set(item)
        qs_dump = qs_db_model.model_dump()
        qs_dump['questions'] = [q.id for q in qs_db_model.questions] # Normalize questions to IDs
        all_data["question_set"][item.id] = qs_dump

    # Fetch all Course items
    course_items = db.session.query(SQLCourse).all()
    for item in course_items:
        course_db_model = db_manager._hydrate_course(item)
        course_dump = course_db_model.model_dump()
        course_dump['question_sets'] = [qs.id for qs in course_db_model.question_sets] # Normalize question_sets to IDs
        all_data["course"][item.id] = course_dump

    # Ensure the config directory exists
    os.makedirs(CONFIG_FOLDER, exist_ok=True)

    with open(JSON_DUMP_FILE, 'w') as f:
        json.dump(all_data, f, indent=4)
    
    print(f"Database content saved to {JSON_DUMP_FILE}")

if __name__ == '__main__':
    app = create_app()
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": os.getenv('DATABASE_URL'),
    })

    with app.app_context():
        save_db_to_json()
