# Backend for Coding Practice Platform

## Overview

This project provides the backend services for a coding practice platform. It's built with Flask, SQLAlchemy for database management, and Pydantic for data validation and serialization. The backend exposes various API endpoints to serve course content, questions, learn materials, and handles code submissions. It also includes utility scripts for easy database management via JSON files.

## Features

*   **API Endpoints**: Provides structured data for courses, question sets, individual questions, and learn content.
*   **Type-Safe Responses**: Uses Pydantic models to ensure API responses adhere to defined data shapes.
*   **Database Management**: Utilizes SQLAlchemy for robust and type-safe interaction with a SQLite database.
*   **JSON-based Database Utilities**: Scripts to easily save the entire database content to a JSON file and load it back, facilitating content management for non-technical users.
*   **CORS Support**: Configured for cross-origin resource sharing to allow frontend applications to connect.

## Project Structure

The project is organized as follows:

*   `app.py`:
    *   The main Flask application entry point.
    *   Initializes the Flask app, CORS, SQLAlchemy, and registers all API blueprints.
    *   Includes a `flask init-db` command to create database tables.
*   `db.py`:
    *   Initializes the SQLAlchemy database instance (`db`). This is kept separate to avoid circular imports.
*   `lib/`: Contains core logic and shared modules.
    *   `lib/database_manager.py`:
        *   Encapsulates all database CRUD (Create, Read, Update, Delete) operations.
        *   Provides methods to interact with the database using Pydantic `database_models`.
        *   Handles ID generation for new entries.
    *   `lib/models/`: Contains Pydantic and SQLAlchemy model definitions.
        *   `lib/models/SQLmodels.py`: Defines the SQLAlchemy database schema (tables, columns, relationships).
        *   `lib/models/database_models.py`: Pydantic models that mirror the SQLAlchemy models. Used as input/output for `DatabaseManager`.
        *   `lib/models/response_models.py`: Pydantic models defining the structure of API responses, tailored for the frontend.
    *   `lib/transformers.py`:
        *   Contains functions to transform data from `database_models` (internal DB representation) to `response_models` (frontend API representation).
*   `routes/`: Contains Flask Blueprints, each defining a set of related API endpoints.
    *   `routes/base_content.py`: Handles the `/base-content` endpoint, returning a default set of courses and learn content.
    *   `routes/learn_routes.py`: Handles the `/learn/<learn_id>` endpoint, returning details for a specific learn item.
    *   `routes/question_set_routes.py`: Handles the `/question-set/<question_set_id>` endpoint, returning details for a specific question set.
    *   `routes/question_details_routes.py`: Handles the `/question-details/<question_id>` endpoint, returning full details for a specific question.
    *   `routes/submit.py`: Handles the `/submit` endpoint for code submission (existing functionality).
*   `config/`: Stores configuration files.
    *   `config/db_dump.json`: A JSON file containing a dump of the database content, used by `save_db_to_json.py` and `load_db_from_json.py`.
    *   `config/default_content.json`: Configures the IDs of content (courses, learn items) to be returned by the `/base-content` endpoint.
*   `test/`: Contains scripts for testing and populating the database.
    *   `test/test_database.py`: A script to populate the database with sample data from `test/testJSON.json` and verify its integrity.
    *   `test/test.py`: A script to test the functionality of various API endpoints by making HTTP requests.
    *   `test/testJSON.json`: Sample JSON data used by `test/test_database.py`.
*   `.env`: Environment variables for configuration (e.g., `DATABASE_URL`, `FRONTEND_ORIGIN`, `SECRET_KEY`).
*   `requirements.txt`: Lists all Python dependencies required by the project.
*   `save_db_to_json.py`: A standalone script to export the entire database content into `config/db_dump.json`.
*   `load_db_from_json.py`: A standalone script to import content from `config/db_dump.json` into the database.
*   `db_structure_explanation.md`: Explains the structure of the `db_dump.json` file.

## Setup

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure environment variables**:
    *   Create a `.env` file in the project root (`backend/`) if it doesn't exist.
    *   Add the following variables:
        ```
        FLASK_DEBUG=True
        PORT=5000
        DATABASE_URL="sqlite:///project.db"
        FRONTEND_ORIGIN="http://localhost:5173" # Or your frontend's URL
        SECRET_KEY="your_secret_key_here" # Change this to a strong, random key
        ```
5.  **Initialize the database**:
    ```bash
    flask init-db
    ```
    This command creates the `project.db` file (in the `instance/` folder) and all necessary tables.

## Database Management

*   **Populate with test data**:
    ```bash
    python3 -m test.test_database
    ```
    This script will clear the database, then add sample `Learn`, `Question`, `QuestionSet`, and `Course` data from `test/testJSON.json`.
*   **Save current database to JSON**:
    ```bash
    python3 save_db_to_json.py
    ```
    This will create/update `config/db_dump.json` with the current state of your database.
*   **Load database from JSON**:
    ```bash
    python3 load_db_from_json.py
    ```
    This will clear your current database and populate it with content from `config/db_dump.json`.

## Running the Application

To start the Flask development server:

```bash
flask run
```
The server will typically run on `http://127.0.0.1:5000`.

## API Endpoints

*   `GET /base-content`: Returns a `ContentSet` containing default courses and learn content.
*   `GET /learn/<learn_id>`: Returns details for a specific learn item.
*   `GET /question-set/<question_set_id>`: Returns details for a specific question set.
*   `GET /question-details/<question_id>`: Returns full details for a specific question.
*   `POST /submit`: Handles code submissions (existing functionality).

## Testing API Endpoints

To test the API endpoints directly:

```bash
python3 test/test.py
```
This script will make HTTP requests to the running Flask server and print the responses.


## if nothing works
end the flask session
delete the project.db
and restart everything
ensure the data is saved in the json dump