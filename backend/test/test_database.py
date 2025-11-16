import json
import os
from app import create_app
from db import db
from lib.database_manager import db_manager
from lib.models.database_models import LearnDB, QuestionDB, FileContentDB, TestCaseDB, HintDB, CourseDB, QuestionSetDB

def run_database_test():
    """
    Adds content from the JSON file to the database and verifies it.
    """
    # 1. Load the test JSON data
    json_path = os.path.join(os.path.dirname(__file__), 'testJSON.json')
    with open(json_path, 'r') as f:
        test_data = json.load(f)

    # 2. Add a 'Learn' item
    learn_json = test_data['learn']['learn_id']
    learn_to_add = {k: v for k, v in learn_json.items() if k != 'learn_id'}
    learn_pdb = LearnDB(**learn_to_add)
    
    print("\n--- Adding Learn item ---")
    created_learn = db_manager.add_learn(learn_pdb)
    assert created_learn.id is not None
    assert created_learn.title == learn_json['title']
    print(f"Successfully added Learn item with ID: {created_learn.id}")

    # 3. Verify the 'Learn' item was added
    retrieved_learn = db_manager.get_learn(created_learn.id)
    assert retrieved_learn is not None
    assert retrieved_learn.title == learn_json['title']
    print(f"Successfully verified Learn item with ID: {retrieved_learn.id}")

    # 4. Add a 'Question' item
    question_json = test_data['question']['question_id']
    question_json['learn_id'] = created_learn.id # Link to the newly created learn item
    
    # Create Pydantic models for nested objects, assigning the correct question_id
    files_pdb = [FileContentDB(**f, question_id=created_learn.id) for f in question_json['base_files']]
    hints_pdb = [HintDB(text=h, question_id=created_learn.id) for h in question_json['hints']]
    test_cases_pdb = [TestCaseDB(**tc, question_id=created_learn.id) for tc in question_json['test_cases']]

    question_to_add = {
        "name": question_json['question_name'],
        "difficulty": question_json['question_difficulty'],
        "details": question_json['question_details'],
        "answer": question_json['answer'],
        "learn_id": question_json['learn_id'],
        "files": files_pdb,
        "hints": hints_pdb,
        "test_cases": test_cases_pdb,
    }
    question_pdb = QuestionDB(**question_to_add)

    print("\n--- Adding Question item ---")
    created_question = db_manager.add_question(question_pdb)
    assert created_question.id is not None
    assert created_question.name == question_json['question_name']
    assert len(created_question.files) == 1
    print(f"Successfully added Question item with ID: {created_question.id}")

    # 5. Verify the 'Question' item was added
    retrieved_question = db_manager.get_question(created_question.id)
    assert retrieved_question is not None
    assert retrieved_question.name == question_json['question_name']
    assert retrieved_question.learn_id == created_learn.id
    assert retrieved_question.files[0].file_name == "main.java"
    print(f"Successfully verified Question item with ID: {retrieved_question.id}")

    # 6. Add a 'Course' item that contains the question
    course_json = test_data['course']['course_id']
    qs_json = course_json['question_sets'][0]

    # We need to provide the full question data, not just the summary
    question_set_to_add = {
        "name": qs_json['name'],
        "questions": [created_question] # Use the full question object we created
    }
    
    course_to_add = {
        "name": course_json['course_name'],
        "description": course_json['description'],
        "question_sets": [question_set_to_add]
    }
    course_pdb = CourseDB(**course_to_add)

    print("\\n--- Adding Course item ---")
    created_course = db_manager.add_course(course_pdb)
    assert created_course.id is not None
    assert created_course.name == course_json['course_name']
    assert len(created_course.question_sets) == 1
    assert created_course.question_sets[0].questions[0].name == created_question.name
    print(f"Successfully added Course item with ID: {created_course.id}")

    # 7. Verify the 'Course' item was added
    retrieved_course = db_manager.get_course(created_course.id)
    assert retrieved_course is not None
    assert retrieved_course.name == course_json['course_name']
    print(f"Successfully verified Course item with ID: {retrieved_course.id}")

    # 8. Add a standalone 'QuestionSet' item
    qs_json = test_data['question_set']['question_set_id']
    qs_to_add = {
        "name": qs_json['name'],
        "questions": [created_question]
    }
    qs_pdb = QuestionSetDB(**qs_to_add)
    print("\\n--- Adding Standalone QuestionSet item ---")
    created_qs = db_manager.add_question_set(qs_pdb)
    assert created_qs.id is not None
    assert created_qs.name == qs_json['name']
    print(f"Successfully added QuestionSet item with ID: {created_qs.id}")

    print("\\n--- All content added and verified successfully! ---")

if __name__ == '__main__':
    app = create_app()
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": os.getenv('DATABASE_URL'), # Use the actual database
    })

    with app.app_context():
        # For a clean test, we clear the DB first.
        # In a real scenario, you might want to avoid this.
        print("--- Clearing and re-initializing database for test ---")
        db.drop_all()
        db.create_all()
        
        # Run the function to add and verify content
        run_database_test()

