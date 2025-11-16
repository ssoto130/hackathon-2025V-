from db import db
from lib.models.SQLmodels import Course as SQLCourse, QuestionSet as SQLQuestionSet, Question as SQLQuestion, Learn as SQLLearn, FileContent as SQLFileContent, TestCase as SQLTestCase, Hint as SQLHint
from lib.models.database_models import CourseDB, QuestionSetDB, QuestionDB, LearnDB, FileContentDB, TestCaseDB, HintDB

class DatabaseManager:
    # id generator 
    def _generate_id(self, prefix: str, model_class) -> str:
        """Generates a new prefixed string ID (e.g., 'c1', 'q2')."""
        count = db.session.query(model_class).count()
        return f"{prefix}{count + 1}"

    # hydrate (SQLAlchemy -> Pydantic) 

    def _hydrate_learn(self, learn_sql: SQLLearn) -> LearnDB:
        return LearnDB.model_validate(learn_sql)

    def _hydrate_file_content(self, file_sql: SQLFileContent) -> FileContentDB:
        return FileContentDB.model_validate(file_sql)

    def _hydrate_test_case(self, test_case_sql: SQLTestCase) -> TestCaseDB:
        return TestCaseDB.model_validate(test_case_sql)

    def _hydrate_hint(self, hint_sql: SQLHint) -> HintDB:
        return HintDB.model_validate(hint_sql)

    def _hydrate_question(self, question_sql: SQLQuestion) -> QuestionDB:
        return QuestionDB(
            id=question_sql.id,
            name=question_sql.name,
            difficulty=question_sql.difficulty,
            details=question_sql.details,
            answer=question_sql.answer,
            learn_id=question_sql.learn_id,
            files=[self._hydrate_file_content(f) for f in question_sql.files],
            test_cases=[self._hydrate_test_case(tc) for tc in question_sql.test_cases],
            hints=[self._hydrate_hint(h) for h in question_sql.hints]
        )

    def _hydrate_question_set(self, qs_sql: SQLQuestionSet) -> QuestionSetDB:
        return QuestionSetDB(
            id=qs_sql.id,
            name=qs_sql.name,
            questions=[self._hydrate_question(q) for q in qs_sql.questions]
        )

    def _hydrate_course(self, course_sql: SQLCourse) -> CourseDB:
        return CourseDB(
            id=course_sql.id,
            name=course_sql.name,
            description=course_sql.description,
            question_sets=[self._hydrate_question_set(qs) for qs in course_sql.question_sets]
        )

    # get and add for each content piece

    def get_learn(self, learn_id: str) -> LearnDB | None:
        learn_sql = db.session.get(SQLLearn, learn_id)
        return self._hydrate_learn(learn_sql) if learn_sql else None

    def add_learn(self, learn_data: LearnDB) -> LearnDB:
        new_id = self._generate_id('l', SQLLearn)
        new_learn_sql = SQLLearn(id=new_id, **learn_data.model_dump(exclude={'id'}))
        db.session.add(new_learn_sql)
        db.session.commit()
        return self._hydrate_learn(new_learn_sql)

    def get_question(self, question_id: str) -> QuestionDB | None:
        question_sql = db.session.get(SQLQuestion, question_id)
        return self._hydrate_question(question_sql) if question_sql else None

    def add_question(self, question_data: QuestionDB) -> QuestionDB:
        new_id = self._generate_id('q', SQLQuestion)
        new_question_sql = SQLQuestion(id=new_id, **question_data.model_dump(exclude={'id', 'files', 'test_cases', 'hints'}))

        for file_data in question_data.files:
            file_id = self._generate_id('f', SQLFileContent)
            new_question_sql.files.append(SQLFileContent(id=file_id, **file_data.model_dump(exclude={'id'})))
        for tc_data in question_data.test_cases:
            tc_id = self._generate_id('tc', SQLTestCase)
            new_question_sql.test_cases.append(SQLTestCase(id=tc_id, **tc_data.model_dump(exclude={'id'})))
        for hint_data in question_data.hints:
            hint_id = self._generate_id('h', SQLHint)
            new_question_sql.hints.append(SQLHint(id=hint_id, **hint_data.model_dump(exclude={'id'})))

        db.session.add(new_question_sql)
        db.session.commit()
        return self._hydrate_question(new_question_sql)

    def get_question_set(self, qs_id: str) -> QuestionSetDB | None:
        qs_sql = db.session.get(SQLQuestionSet, qs_id)
        return self._hydrate_question_set(qs_sql) if qs_sql else None

    def add_question_set(self, qs_data: QuestionSetDB) -> QuestionSetDB:
        new_id = self._generate_id('qs', SQLQuestionSet)
        new_qs_sql = SQLQuestionSet(id=new_id, **qs_data.model_dump(exclude={'id', 'questions'}))

        for q_data in qs_data.questions:
            if q_data.id:
                question_sql = db.session.get(SQLQuestion, q_data.id)
                if question_sql:
                    new_qs_sql.questions.append(question_sql)
        
        db.session.add(new_qs_sql)
        db.session.commit()
        return self._hydrate_question_set(new_qs_sql)

    def get_course(self, course_id: str) -> CourseDB | None:
        course_sql = db.session.get(SQLCourse, course_id)
        return self._hydrate_course(course_sql) if course_sql else None

    def add_course(self, course_data: CourseDB) -> CourseDB:
        new_id = self._generate_id('c', SQLCourse)
        new_course_sql = SQLCourse(id=new_id, **course_data.model_dump(exclude={'id', 'question_sets'}))

        for qs_data in course_data.question_sets: # qs_data is a QuestionSetDB object
            if qs_data.id:
                existing_qs_sql = db.session.get(SQLQuestionSet, qs_data.id)
                if existing_qs_sql:
                    new_course_sql.question_sets.append(existing_qs_sql)
                else:
                    print(f"Warning: QuestionSet with ID '{qs_data.id}' not found in DB when adding course '{new_id}'. Skipping link.")
            else:
                print(f"Error: QuestionSet data without ID passed to add_course for course '{new_id}'. Skipping link.")

        db.session.add(new_course_sql)
        db.session.commit()
        return self._hydrate_course(new_course_sql)

# Single instance to be used by the application
db_manager = DatabaseManager()
