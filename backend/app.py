from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routes.submit import submit_bp
from routes.base_content import base_content_bp
from routes.learn_routes import learn_bp
from routes.question_set_routes import question_set_bp
from routes.question_details_routes import question_details_bp
from db import db
from lib.models.SQLmodels import Course, Question, QuestionSet, Learn, FileContent, TestCase, Hint


load_dotenv()



def create_app():

    app = Flask(__name__)
    CORS(app, origins=[os.getenv('FRONTEND_ORIGIN')])

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(submit_bp)
    app.register_blueprint(base_content_bp)
    app.register_blueprint(learn_bp)
    app.register_blueprint(question_set_bp)
    app.register_blueprint(question_details_bp)

    @app.cli.command("init-db")

    def init_db_command():
        """Clear existing data and create new tables."""
        with app.app_context():
            db.create_all()
        print("Initialized the database.")

    return app

app = create_app()


if __name__ == '__main__':
    app.run(
        debug=os.getenv('FLASK_DEBUG') == 'True',
        port=int(os.getenv('PORT', 5000))
    )
