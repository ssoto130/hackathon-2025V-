# Database JSON Structure Explanation

This document explains the structure of the `db_dump.json` file used for loading and saving the entire database content. The structure is designed to be "normalized," meaning each unique item is stored once, and relationships between items are represented by their unique IDs.

## File Location

The `db_dump.json` file is located in the `config/` folder of the backend project.

## Overall Structure

The JSON file is a single object (dictionary) with top-level keys representing each major content type in the database. Each top-level key contains another dictionary where the keys are the unique IDs of the items, and the values are the item's data.

```json
{
    "learn": {
        "l1": { ... },
        "l2": { ... }
    },
    "question": {
        "q1": { ... },
        "q2": { ... }
    },
    "question_set": {
        "qs1": { ... },
        "qs2": { ... }
    },
    "course": {
        "c1": { ... },
        "c2": { ... }
    }
}
```

## ID Prefixes

Each type of content has a unique ID prefix to make them easily identifiable and to ensure uniqueness across different content types.

| Content Type | ID Prefix | Example ID |
| :----------- | :-------- | :--------- |
| Learn        | `l`       | `l1`, `l2` |
| Question     | `q`       | `q1`, `q2` |
| QuestionSet  | `qs`      | `qs1`, `qs2` |
| Course       | `c`       | `c1`, `c2` |

## Content Type Details and Relationships

Below are the details for each content type, including how their fields are represented and how relationships to other content types are stored.

### `learn`

*   **Key**: `learn`
*   **Structure**: Dictionary of Learn objects, keyed by `learn_id`.
*   **Fields**:
    *   `id`: (string) Unique ID (e.g., `l1`).
    *   `title`: (string) Title of the learn content.
    *   `content`: (string) The main body of the learn content.
*   **Relationships**: None directly within its own structure. Referenced by `Question` objects via `learn_id`.

### `question`

*   **Key**: `question`
*   **Structure**: Dictionary of Question objects, keyed by `question_id`.
*   **Fields**:
    *   `id`: (string) Unique ID (e.g., `q1`).
    *   `name`: (string) Name of the question.
    *   `difficulty`: (string) Difficulty level (e.g., "Easy", "Medium").
    *   `details`: (string) Full description of the question.
    *   `answer`: (string) The correct answer or solution.
    *   `learn_id`: (string) ID of the associated `Learn` object (e.g., `l1`).
    *   `files`: (list of objects) List of `FileContent` objects. Each object has:
        *   `id`: (string) Unique ID (e.g., `f1`).
        *   `file_name`: (string) Name of the file (e.g., "main.java").
        *   `content`: (string) The content of the file.
        *   `editable`: (boolean) Whether the file is editable by the user.
        *   `question_id`: (string) ID of the associated `Question` object (e.g., `q1`).
    *   `hints`: (list of objects) List of `Hint` objects. Each object has:
        *   `id`: (string) Unique ID (e.g., `h1`).
        *   `text`: (string) The hint text.
        *   `question_id`: (string) ID of the associated `Question` object (e.g., `q1`).
    *   `test_cases`: (list of objects) List of `TestCase` objects. Each object has:
        *   `id`: (string) Unique ID (e.g., `tc1`).
        *   `input`: (string) Input for the test case.
        *   `expected_output`: (string) Expected output for the test case.
        *   `question_id`: (string) ID of the associated `Question` object (e.g., `q1`).
*   **Relationships**: References `Learn` by its ID. Contains nested `FileContent`, `Hint`, and `TestCase` objects.

### `question_set`

*   **Key**: `question_set`
*   **Structure**: Dictionary of QuestionSet objects, keyed by `question_set_id`.
*   **Fields**:
    *   `id`: (string) Unique ID (e.g., `qs1`).
    *   `name`: (string) Name of the question set.
    *   `questions`: (list of strings) List of `Question` IDs (e.g., `["q1", "q2"]`).
*   **Relationships**: References `Question` objects by their IDs. Referenced by `Course` objects via `question_set_id`.

### `course`

*   **Key**: `course`
*   **Structure**: Dictionary of Course objects, keyed by `course_id`.
*   **Fields**:
    *   `id`: (string) Unique ID (e.g., `c1`).
    *   `name`: (string) Name of the course.
    *   `description`: (string) Description of the course.
    *   `question_sets`: (list of strings) List of `QuestionSet` IDs (e.g., `["qs1", "qs2"]`).
*   **Relationships**: References `QuestionSet` objects by their IDs.

---

This normalized structure allows for easy editing of individual content items and ensures that changes to a single item (e.g., a Question) are reflected everywhere it's referenced.


## Default content
To have items appear in the home page you must specify them in the config/default_content.json
when the base-content route runs, it will check the default_content, get all IDs from there and send that info to the front end