"""
This module contains functions for transforming data between different model layers,
such as from internal database models (DB) to frontend-facing response models.
"""
from lib.models import response_models as responses
from lib.models import database_models as db_models

def transform_question_db_to_response(question_db: db_models.QuestionDB) -> responses.QuestionSetQuestion:
    """Converts a QuestionDB model to a simplified QuestionSetQuestion response model."""
    return responses.QuestionSetQuestion(
        questionId=str(question_db.id),
        questionName=question_db.name,
        questionDifficulty=question_db.difficulty
    )

def transform_question_set_db_to_response(qs_db: db_models.QuestionSetDB) -> responses.QuestionSet:
    """Converts a QuestionSetDB model to a QuestionSet response model."""
    return responses.QuestionSet(
        type='questionSet',
        questionSetId=str(qs_db.id),
        name=qs_db.name,
        questions=[transform_question_db_to_response(q) for q in qs_db.questions]
    )

def transform_course_db_to_response(course_db: db_models.CourseDB) -> responses.Course:
    """Converts a CourseDB model to a Course response model."""
    return responses.Course(
        type='course',
        courseId=str(course_db.id),
        courseName=course_db.name,
        description=course_db.description,
        questionSets=[transform_question_set_db_to_response(qs) for qs in course_db.question_sets]
    )

def transform_learn_db_to_response(learn_db: db_models.LearnDB) -> responses.Learn:
    """Converts a LearnDB model to a Learn response model."""
    return responses.Learn(
        type='learn',
        learnId=str(learn_db.id),
        title=learn_db.title,
        content=learn_db.content
    )

def transform_question_db_to_full_response(question_db: db_models.QuestionDB, learn_response: responses.Learn) -> responses.Question:
    """Converts a QuestionDB model to a full Question response model."""
    # Transform nested FileContentDB to FileContent
    files_response = [
        responses.FileContent(
            fileName=f.file_name,
            content=f.content,
            editable=f.editable
        ) for f in question_db.files
    ]

    # Transform nested hints (list of strings)
    hints_response = [h.text for h in question_db.hints]

    return responses.Question(
        type='question',
        questionId=str(question_db.id),
        questionDifficulty=question_db.difficulty,
        questionName=question_db.name,
        questionDetails=question_db.details,
        answer=question_db.answer,
        baseFiles=files_response,
        hints=hints_response,
        learn=learn_response
    )