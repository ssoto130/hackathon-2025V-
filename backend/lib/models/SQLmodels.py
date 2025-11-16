from db import db

# Association table for the many-to-many relationship between QuestionSet and Question
question_set_questions = db.Table('question_set_questions',
    db.Column('question_id', db.String(50), db.ForeignKey('question.id'), primary_key=True),
    db.Column('question_set_id', db.String(50), db.ForeignKey('question_set.id'), primary_key=True)
)

# Association table for the many-to-many relationship between Course and QuestionSet
course_question_sets = db.Table('course_question_sets',
    db.Column('question_set_id', db.String(50), db.ForeignKey('question_set.id'), primary_key=True),
    db.Column('course_id', db.String(50), db.ForeignKey('course.id'), primary_key=True)
)

class Learn(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    questions = db.relationship('Question', backref='learn', lazy=True)

class Question(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    learn_id = db.Column(db.String(50), db.ForeignKey('learn.id'), nullable=False)
    files = db.relationship('FileContent', backref='question', lazy=True)
    test_cases = db.relationship('TestCase', backref='question', lazy=True)
    hints = db.relationship('Hint', backref='question', lazy=True)

class FileContent(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    editable = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.String(50), db.ForeignKey('question.id'), nullable=False)

class TestCase(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    input = db.Column(db.Text, nullable=False)
    expected_output = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.String(50), db.ForeignKey('question.id'), nullable=False)

class Hint(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    text = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.String(50), db.ForeignKey('question.id'), nullable=False)

class QuestionSet(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    questions = db.relationship('Question', secondary=question_set_questions, lazy='subquery',
        backref=db.backref('question_sets', lazy=True))

class Course(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    question_sets = db.relationship('QuestionSet', secondary=course_question_sets, lazy='subquery',
        backref=db.backref('courses', lazy=True))
