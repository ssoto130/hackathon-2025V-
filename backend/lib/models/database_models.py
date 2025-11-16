"""the models in which the database is stored as"""
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from lib.models.response_models import QuestionDifficulty

class LearnDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    title: str
    content: str

class FileContentDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    file_name: str
    content: str
    editable: bool
    question_id: str

class TestCaseDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    input: str
    expected_output: str
    question_id: str

class HintDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    text: str
    question_id: str

class QuestionDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    name: str
    difficulty: QuestionDifficulty
    details: str
    answer: str
    learn_id: str
    files: List[FileContentDB] = []
    test_cases: List[TestCaseDB] = []
    hints: List[HintDB] = []

class QuestionSetDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    name: str
    questions: List[QuestionDB] = []

class CourseDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[str] = None
    name: str
    description: str
    question_sets: List[QuestionSetDB] = []
