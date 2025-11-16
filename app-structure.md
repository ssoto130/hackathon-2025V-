# app design

## data storage

This is how the data should be structured in the database.

### courses

a dictionary of courses; the key is `courseId`

```ts
[
  coursId: {
      courseId: string;
      courseName: string;
      description: string;
      weeks: [{
          weekName: string;
          questionSetId: string;
      }]
  }
]
```

#### Example in json format:

```json
[
  {
    "courseId": "course1",
    "courseName": "programming fundamentals 1",
    "description": "start learning java woop",
    "weeks": [
      {
        "weekName": "Week 1: printing to the console",
        "questionSetId": "qs1"
      },
      {
        "weekName": "Week 2: If statements",
        "questionSetId": "qs2"
      }
    ]
  },
  {
    "courseId": "course2",
    "courseName": "programming fundamentals 2",
    "description": "Start getting into java OOP",
    "weeks": [
      {
        "weekName": "Week 1: Java classes",
        "questionSetId": "qs3"
      }
    ]
  }
]
```

### question sets

a dictionary of question sets; the key is `questionSetId`

```ts
{
  questionSetId: {
    questionSetId: string;
    name: string;
    questions: {
      questionId: string;
      questionName: string;
      questionDifficulty: string(Easy | Medium | Hard | Impossible);
    }
    [];
  }
}
```

#### example in json

```json
{
  "qs1": {
    "questionSetId": "qs1",
    "name": "Week 1 practice",
    "questions": [
      {
        "questionId": "q1",
        "questionName": "hello world",
        "questionDifficulty": "Easy"
      },
      {
        "questionId": "q2",
        "questionName": "adding 2 vars",
        "questionDifficulty": "Medium"
      }
    ]
  },
  "qs2": {
    "questionSetId": "qs2",
    "name": "Week 2 practice",
    "questions": [
      {
        "questionId": "q2",
        "questionName": "This is a example",
        "questionDifficulty": "Hard"
      },
      {
        "questionId": "q2",
        "questionName": "More test info",
        "questionDifficulty": "Impossible"
      }
    ]
  }
}
```

### questions

A dictionary of questions; the key is `questionId`.

```ts
{
  questionId: {
  	questionId: string;
  	questionDifficulty: string(Easy | Medium | Hard | Impossible);
  	questionName: string;
  	questionDetails: string;
  	answer: string;
  	baseFiles:
    {
      fileName: string;
      content: string;
      editable: boolean;
    }[];
    testCases:
    {
      input: string;
      expectedOutput: string;
    }[];
  	hints: string[];
  	learnId: string;
  }
}
```

#### Example

```json
{
  "q1": {
    "questionId": "q1",
    "questionDifficulty": "Easy",
    "questionName": "hello world",
    "questionDetails": "write a program that prints hello world to the console",
    "answer": "System.out.println(\"hello world\"); you'd also add explanation here",
    "baseFiles": [
      {
        "fileName": "LearnPrint.java",
        "content": "// Write your code here also add the base class and main method",
        "editable": true
      }
    ],
    "hints": ["you will use System.out.println();"],
    "learnId": "learn-java-print",
    "testCases": [
      {
        "input": "",
        "expectedOutput": "hello world"
      }
    ]
  },
  "q2": {
    "questionId": "q2",
    "questionDifficulty": "Medium",
    "questionName": "adding 2 vars",
    "questionDetails": "write a program that adds 2 variables",
    "answer": "System.out.println(2 + 2);\nyou'd also add explanation here",
    "baseFiles": [
      {
        "fileName": "var_adding.java",
        "content": "print(aaa)",
        "editable": true
      },
      {
        "fileName": "second_test_file.txt",
        "content": "idk it is just for testing",
        "editable": false
      }
    ],
    "hints": ["you will use System.out.println();"],
    "learnId": "learn-java-print",
    "testCases": [
      {
        "input": "1\n2",
        "expectedOutput": "3"
      },
      {
        "input": "3\n5",
        "expectedOutput": "8"
      }
    ]
  }
}
```

### learn

a dictionary of learning content, the key is `learnId`

```ts
{
  learnId: {
    learnId: string;
    content: string;
  }
}
```

````json
{
  "learn-java-print": {
    "learnId": "learn-java-print",
    "content": "The `System.out.println()` method in Java is used to display output to the console."
  },
  "java-if-statements": {
    "learnId": "java-if-statements",
    "content": "do: ```java\nif(statement) \n{code to run}```"
  }
}
````

## routing

The routes of the app uses

### api routes

these are the routes and what they are expected to return, the routes dont need to be exact, these routes are just what the svelte project uses but the backend can use /courses rather than /api/courses for example, anything in [] are variables
to make the program more effecient we **may** add parameters to get the default items in the same request, these would be things like `/question-set-/[questionSetId]?question=[questionId]

#### /api/courses - gets the course information

```ts
{
    courseId: string;
    courseName: string;
    description: string;
    weeks: [{
        weekName: string;
        questionSetId: string;
    }]
}
```

#### /api/question-set/[questionSetId] - gets the question set from questionSetId

```ts
{
  questionSetId: string;
  name: string;
  questions: {
    questionId: string;
    questionName: string;
    questionDifficulty: String(Easy | Medium | Hard | Impossible);
  }
  [];
}
```

#### /api/question-details/[questionId] - gets the question info from questionId

```ts
{
    questionId: string;
    questionDifficulty: questionDifficulty,
    questionName: string;
    questionDetails: string;
    answer: string;
    baseFiles: [
      {
        fileName: string;
        content: string;
        editable: boolean;
      }
    ];
    hints: string[];
    learn: {
      learnId: string;
      content: string;
    };
}
```

#### /api/learn/[learnId] - gets the info related to the learn content

```ts
{
  learnId: string;
  content: string;
}
```

#### /api/submit

this is the only request that would send info
the info sent would be structured like this:

```ts
{
  questionId: string;
  files:[
    {
      fileName: string;
      content: string;
    }
  ]
}
```

and it will expect this response:

```ts
{
  input: string;
  result: string;
  expectedResult: string;
  passedTests: boolean;
  error: string | null;
}
```

#### example

```json
{
  "input": "2 3",
  "result": "4",
  "expectedResult": "5",
  "passedTests": false,
  "error": undefined
}
```

if there is no input it should just be a empty string, this is to avoid null, since null is a pain to deal with

### page routes

these are the routes of the website itself, and the pages it has, the info gets and such, this may be outdated

#### `/` — Home Page

- Displays the list of **courses** and **weeks**.
- params:
  - course: courseId - this effects the default shown course
- **`+page.server.ts`**
  - Fetches the course list and default week list.
  - Sends the data to the home page for rendering.
- sends to:
  - the week list sends to /problems/
  - sends to /learn/ via small button on the list
- requests:
  - fetches week info (/api/weeks/[courseId]) when the selected course changes

#### '/problems/[questionSetId]' - question solving and selecting page

- the [page](/design/code_page.png) where a user may select a question and solve them
- params:
  - question: questionId - this loads the question for the questionId, otherwise does a default first
- server.ts
  - fetches the questionList questions along with the question info for the page
- sends to:
  - home button sends to /
  - expand button on learn tab sends to /learn/
- requests:
  - fetches question details (/api/question-data/[questionId]) when the selected question changes

#### '/learn/[learnId]' - learning page

- this will basically be a full page version of the learn tab that exists on the /problems/page
- the learn page will teach x topic such as if statements etc
- server.ts
  - gets the learn markdown
- sends to:
  - home button sends to /
  - buttons to go to next or previous page/week in the course?

## Cookies

this is outdated

while or if we dont use accounts we want some way to store info for each user

```json
{
  "selectedCourse": "courseId - stores the last selected course"
  "questions": {
    "questionId": {
      "completed": "bool"
      "codeDone": "string - the code the user has so far put in the question"
    }
  }
}
```

## potential features

- progress bar per week
  - would require having the courseId to get the questionId so we can check via user cookies though

- accounts:
  - stores the % completed for questions
  - the code for each question

- if we add user made questionts reorganize the home menu for more intuitive ui
  - the home page will be more general which can then link to the courses page, make a question page among other things

- ai
  - the user can talk and interact with ai in a panel, or ask it to clarify terminal errors
  - a user can have it help them make questions

### pages

- account page, this is where you can view the problems made and other acc info
- a page to make, edit, save problems
