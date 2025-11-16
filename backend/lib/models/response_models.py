"""the format of which responses should be made in"""
from enum import Enum
from typing import List, Literal, Optional, Union
from pydantic import BaseModel


class QuestionDifficulty(str, Enum):
    """question difficulty enum"""
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'
    IMPOSSIBLE = 'Impossible'


class FileContent(BaseModel):
    """file content model"""
    fileName: str
    content: str
    editable: bool


class Learn(BaseModel):
    """learn model"""
    type: Literal['learn']
    learnId: str
    title: str
    content: str


class Question(BaseModel):
    """question model"""
    type: Literal['question']
    questionId: str
    questionDifficulty: QuestionDifficulty
    questionName: str
    questionDetails: str
    answer: str
    baseFiles: List[FileContent]
    hints: List[str]
    learn: Learn


class TestCase(BaseModel):
    """test case model"""
    input: str
    expectedOutput: str


class QuestionSetQuestion(BaseModel):
    """question set question model"""
    questionId: str
    questionName: str
    questionDifficulty: QuestionDifficulty


class QuestionSet(BaseModel):
    """question set model"""
    type: Literal['questionSet']
    questionSetId: str
    name: str
    questions: List[QuestionSetQuestion]


class Course(BaseModel):
    """course model"""
    type: Literal['course']
    courseId: str
    courseName: str
    description: str
    questionSets: List[QuestionSet]


class ContentSet(BaseModel):
    type: Literal['contentSet']
    content: List[Union[Course, QuestionSet, QuestionSetQuestion, Learn]]


class SubmitResults(BaseModel):
    """submit results model"""
    input: str
    result: str
    expectedResult: str
    passedTests: bool
    error: Optional[str] = None
