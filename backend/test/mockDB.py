FAKE_DB = {
    "courses": [
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
                },
                {
                    "weekName": "Week 3: Loops",
                    "questionSetId": "qs3"
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
                    "questionSetId": "qs4"
                }
            ]
        },
        {
            "courseId": "course3",
            "courseName": "Java Fundamentals Mastery",
            "description": "Master the basics of Java programming with enhanced exercises",
            "weeks": [
                {
                    "weekName": "Week 1: Enhanced Output & Print Statements",
                    "questionSetId": "qs3"
                }
            ]
        }
    ],
    "questionSets": {
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
            "name": "Week 2: If Statements",
            "questions": [
                {
                    "questionId": "q3",
                    "questionName": "basic if statement", 
                    "questionDifficulty": "Easy"
                },
                {
                    "questionId": "q4",
                    "questionName": "if-else conditions",
                    "questionDifficulty": "Medium"
                }
            ]
        },
        "qs3": {
            "questionSetId": "qs3",
            "name": "Week 3: Loops Practice",
            "questions": [
                {
                    "questionId": "q3",
                    "questionName": "For Loop Counting",
                    "questionDifficulty": "Easy"
                },
                {
                    "questionId": "q4", 
                    "questionName": "While Loop Sum",
                    "questionDifficulty": "Medium"
                },
                {
                    "questionId": "q5",
                    "questionName": "Nested Loops Pattern", 
                    "questionDifficulty": "Hard"
                }
            ]
        },
        "qs4": {
            "questionSetId": "qs4",
            "name": "Java Classes Practice", 
            "questions": [
                {
                    "questionId": "q6",
                    "questionName": "Simple Class Creation",
                    "questionDifficulty": "Medium"
                },
                {
                    "questionId": "q6",
                    "questionName": "Personal Greeting",
                    "questionDifficulty": "Easy"
                },
                {
                    "questionId": "q7",
                    "questionName": "Multiple Output Lines",
                    "questionDifficulty": "Medium"
                }
            ]
        }
    },
    "questions": {
        "q1": {
            "questionId": "q1",
            "questionDifficulty": "Easy",
            "questionName": "Your First Java Program: Hello World!",
            "questionDetails": "Welcome to Java programming! Your first task is to create a complete Java program that outputs the phrase \"Hello World!\" to the console. This is a classic beginner exercise that will teach you the basic structure of a Java program.\n\nYou need to:\n1. Create a public class named 'HelloWorld'\n2. Include the main method (the entry point of your program)\n3. Use System.out.println() to print \"Hello World!\" exactly as shown\n\nRemember: Java is case-sensitive, so make sure your capitalization matches exactly!",
            "answer": "```java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World!\");\n    }\n}\n```\n\n**Explanation:**\n- `public class HelloWorld` - Declares a public class named HelloWorld\n- `public static void main(String[] args)` - The main method where program execution begins\n- `System.out.println(\"Hello World!\");` - Prints the text to the console with a new line\n- Don't forget the semicolon (;) at the end of statements!\n- The text must be enclosed in double quotes\n- Java is case-sensitive, so \"Hello World!\" must match exactly",
            "baseFiles": [
                {
                    "fileName": "HelloWorld.java",
                    "content": "public class HelloWorld {\n    public static void main(String[] args) {\n        // TODO: Add your System.out.println statement here\n        // Print \"Hello World!\" to the console\n        \n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use System.out.println() to print text to the console",
                "The text \"Hello World!\" must be enclosed in double quotes",
                "Don't forget the semicolon (;) at the end of your statement", 
                "Make sure the capitalization matches exactly: \"Hello World!\"",
                "The complete statement should look like: System.out.println(\"Hello World!\");"
            ],
            "learnId": "learn-java-print",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "Hello World!\n"
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
                    "editable": True
                },
                {
                    "fileName": "second_test_file.txt",
                    "content": "idk it is just for testing", 
                    "editable": False
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
        },
        "q3": {
            "questionId": "q3",
            "questionDifficulty": "Easy",
            "questionName": "basic if statement",
            "questionDetails": "Write a Java program that checks if a number is positive. Read an integer from input and print 'positive' if the number is greater than 0, otherwise print 'not positive'.",
            "answer": "```java\nimport java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        int number = scanner.nextInt();\n        \n        if (number > 0) {\n            System.out.println(\"positive\");\n        } else {\n            System.out.println(\"not positive\");\n        }\n        \n        scanner.close();\n    }\n}\n```\n\nExplanation: We use Scanner to read input, then use an if-else statement to check if the number is positive.",
            "baseFiles": [
                {
                    "fileName": "PositiveCheck.java",
                    "content": "import java.util.Scanner;\n\npublic class PositiveCheck {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        // Read an integer from input\n        int number = scanner.nextInt();\n        \n        // TODO: Write your if statement here\n        // Check if number > 0 and print appropriate message\n        \n        scanner.close();\n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use 'if (condition)' to check if the number is greater than 0",
                "Remember to print 'positive' or 'not positive' based on the condition",
                "Don't forget the else clause for when the condition is false"
            ],
            "learnId": "learn-java-if-statements",
            "testCases": [
                {
                    "input": "5",
                    "expectedOutput": "positive"
                },
                {
                    "input": "-3",
                    "expectedOutput": "not positive"
                },
                {
                    "input": "0",
                    "expectedOutput": "not positive"
                }
            ]
        },
        "q3": {
            "questionId": "q3", 
            "questionDifficulty": "Easy",
            "questionName": "For Loop Counting",
            "questionDetails": "Write a Java program that uses a for loop to print numbers from 1 to 5.\n\nYour program should:\n1. Use a for loop that starts at 1\n2. Loop until the number is less than or equal to 5\n3. Print each number on a separate line\n\nExpected output:\n```\n1\n2\n3\n4\n5\n```",
            "answer": "```java\npublic class ForLoopCount {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 5; i++) {\n            System.out.println(i);\n        }\n    }\n}\n```\n\n**Explanation:**\n- `for (int i = 1; i <= 5; i++)` - Loop from 1 to 5\n- `int i = 1` - Initialize counter to 1\n- `i <= 5` - Continue while i is less than or equal to 5\n- `i++` - Increment i by 1 each iteration\n- `System.out.println(i)` - Print the current value of i",
            "baseFiles": [
                {
                    "fileName": "ForLoopCount.java",
                    "content": "public class ForLoopCount {\n    public static void main(String[] args) {\n        // TODO: Write a for loop to print numbers 1 to 5\n        \n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use a for loop: for (int i = 1; i <= 5; i++)",
                "Inside the loop, use System.out.println(i) to print each number", 
                "The loop variable should start at 1 and go up to 5",
                "Don't forget the semicolons in your for loop syntax"
            ],
            "learnId": "learn-java-loops",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "1\n2\n3\n4\n5"
                }
            ]
        },
        "q4": {
            "questionId": "q4",
            "questionDifficulty": "Medium",
            "questionName": "While Loop Sum", 
            "questionDetails": "Write a Java program that uses a while loop to calculate the sum of numbers from 1 to 10.\n\nYour program should:\n1. Initialize a sum variable to 0\n2. Use a counter starting at 1\n3. Use a while loop to add numbers 1 through 10\n4. Print the final sum (which should be 55)\n\nExpected output:\n```\n55\n```",
            "answer": "```java\npublic class WhileLoopSum {\n    public static void main(String[] args) {\n        int sum = 0;\n        int i = 1;\n        \n        while (i <= 10) {\n            sum += i;\n            i++;\n        }\n        \n        System.out.println(sum);\n    }\n}\n```\n\n**Explanation:**\n- `int sum = 0` - Initialize sum to zero\n- `int i = 1` - Initialize counter to 1\n- `while (i <= 10)` - Continue while i is less than or equal to 10\n- `sum += i` - Add current value of i to sum\n- `i++` - Increment counter\n- Final sum of 1+2+3+...+10 = 55",
            "baseFiles": [
                {
                    "fileName": "WhileLoopSum.java",
                    "content": "public class WhileLoopSum {\n    public static void main(String[] args) {\n        // TODO: Use a while loop to calculate sum of 1 to 10\n        int sum = 0;\n        int i = 1;\n        \n        // Your while loop here\n        \n        System.out.println(sum);\n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Initialize: int sum = 0; int i = 1;",
                "While condition: while (i <= 10)",
                "Inside loop: sum += i; and i++;",
                "The sum of 1+2+3+...+10 equals 55"
            ],
            "learnId": "learn-java-loops",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "55"
                }
            ]
        },
        "q5": {
            "questionId": "q5",
            "questionDifficulty": "Hard", 
            "questionName": "Nested Loops Pattern",
            "questionDetails": "Write a Java program that uses nested loops to create a right triangle pattern with asterisks.\n\nYour program should create this pattern:\n```\n*\n**\n***\n****\n*****\n```\n\nRequirements:\n1. Use nested for loops\n2. Outer loop controls the rows (1 to 5)\n3. Inner loop prints the asterisks for each row\n4. Each row should end with a newline",
            "answer": "```java\npublic class NestedPattern {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 5; i++) {\n            for (int j = 1; j <= i; j++) {\n                System.out.print(\"*\");\n            }\n            System.out.println();\n        }\n    }\n}\n```\n\n**Explanation:**\n- Outer loop `for (int i = 1; i <= 5; i++)` - Controls rows 1 to 5\n- Inner loop `for (int j = 1; j <= i; j++)` - Prints i asterisks in row i\n- `System.out.print(\"*\")` - Print asterisk without newline\n- `System.out.println()` - Print newline after each row",
            "baseFiles": [
                {
                    "fileName": "NestedPattern.java",
                    "content": "public class NestedPattern {\n    public static void main(String[] args) {\n        // TODO: Use nested loops to create a triangle pattern\n        // Outer loop for rows (1 to 5)\n        // Inner loop for asterisks in each row\n        \n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use two nested for loops",
                "Outer loop: for (int i = 1; i <= 5; i++)",
                "Inner loop: for (int j = 1; j <= i; j++)", 
                "Use System.out.print(\"*\") for asterisks, System.out.println() for new lines"
            ],
            "learnId": "learn-java-loops",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "*\n**\n***\n****\n*****"
                }
            ]
        },
        "q6": {
            "questionId": "q6",
            "questionDifficulty": "Medium",
            "questionName": "if-else conditions",
            "questionDetails": "Write a Java program that categorizes a student's grade. Read an integer score (0-100) and print:\n- 'A' for scores 90-100\n- 'B' for scores 80-89\n- 'C' for scores 70-79\n- 'D' for scores 60-69\n- 'F' for scores below 60",
            "answer": "```java\nimport java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        int score = scanner.nextInt();\n        \n        if (score >= 90) {\n            System.out.println(\"A\");\n        } else if (score >= 80) {\n            System.out.println(\"B\");\n        } else if (score >= 70) {\n            System.out.println(\"C\");\n        } else if (score >= 60) {\n            System.out.println(\"D\");\n        } else {\n            System.out.println(\"F\");\n        }\n        \n        scanner.close();\n    }\n}\n```\n\nExplanation: We use multiple if-else statements to check score ranges in descending order.",
            "baseFiles": [
                {
                    "fileName": "GradeCalculator.java",
                    "content": "import java.util.Scanner;\n\npublic class GradeCalculator {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        int score = scanner.nextInt();\n        \n        // TODO: Write your if-else chain here\n        // Check score ranges and print appropriate grade\n        \n        scanner.close();\n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use if-else if-else chain for multiple conditions",
                "Check from highest score to lowest (90, 80, 70, 60)",
                "Use >= operator to check if score meets the minimum for each grade"
            ],
            "learnId": "learn-java-if-statements",
            "testCases": [
                {
                    "input": "95",
                    "expectedOutput": "A"
                },
                {
                    "input": "85",
                    "expectedOutput": "B"
                },
                {
                    "input": "75",
                    "expectedOutput": "C"
                },
                {
                    "input": "65",
                    "expectedOutput": "D"
                },
                {
                    "input": "45",
                    "expectedOutput": "F"
                }
            ]
        },
        "q5": {
            "questionId": "q5",
            "questionDifficulty": "Easy",
            "questionName": "Enhanced Hello World",
            "questionDetails": "Create a complete Java program that prints 'Hello, World!' to the console. This is your first step into Java programming! Make sure to include the proper class structure and main method.",
            "answer": "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}\n```\n\nExplanation:\n- `public class Main` defines a public class named Main\n- `public static void main(String[] args)` is the main method where program execution begins\n- `System.out.println()` prints text to the console followed by a new line\n- Remember to end statements with semicolons!",
            "baseFiles": [
                {
                    "fileName": "Main.java",
                    "content": "public class Main {\n    public static void main(String[] args) {\n        // TODO: Write your println statement here\n        // Print \"Hello, World!\" to the console\n        \n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use System.out.println() to print to the console",
                "Remember to put your text in double quotes",
                "Don't forget the semicolon at the end of the statement",
                "The text should be exactly 'Hello, World!' with proper capitalization"
            ],
            "learnId": "learn-java-print-enhanced",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "Hello, World!"
                }
            ]
        },
        "q6": {
            "questionId": "q6",
            "questionDifficulty": "Easy",
            "questionName": "Personal Greeting",
            "questionDetails": "Write a Java program that prints a personalized greeting. Print 'Hello, [YourName]!' where [YourName] is replaced with your actual name. For this exercise, use 'Student' as the name.",
            "answer": "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Student!\");\n    }\n}\n```\n\nExplanation: This builds on the basic Hello World by customizing the greeting message.",
            "baseFiles": [
                {
                    "fileName": "Greeting.java",
                    "content": "public class Greeting {\n    public static void main(String[] args) {\n        // TODO: Print a personalized greeting\n        // Use \"Hello, Student!\" as the message\n        \n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use System.out.println() to print the greeting",
                "The message should be 'Hello, Student!' exactly",
                "Remember proper capitalization and punctuation"
            ],
            "learnId": "learn-java-print-enhanced",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "Hello, Student!"
                }
            ]
        },
        "q7": {
            "questionId": "q7",
            "questionDifficulty": "Medium",
            "questionName": "Multiple Output Lines",
            "questionDetails": "Write a Java program that prints multiple lines of output. Your program should print:\nLine 1: 'Welcome to Java Programming!'\nLine 2: 'This is line 2'\nLine 3: 'Programming is fun!'",
            "answer": "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Welcome to Java Programming!\");\n        System.out.println(\"This is line 2\");\n        System.out.println(\"Programming is fun!\");\n    }\n}\n```\n\nExplanation: Each println() statement creates a new line of output. You can call println() multiple times to create multiple lines.",
            "baseFiles": [
                {
                    "fileName": "MultiLine.java",
                    "content": "public class MultiLine {\n    public static void main(String[] args) {\n        // TODO: Print three lines of output\n        // Line 1: Welcome to Java Programming!\n        // Line 2: This is line 2  \n        // Line 3: Programming is fun!\n        \n    }\n}",
                    "editable": True
                }
            ],
            "hints": [
                "Use three separate System.out.println() statements",
                "Each println() will create a new line",
                "Make sure the text matches exactly as specified",
                "Remember proper capitalization and punctuation"
            ],
            "learnId": "learn-java-print-enhanced",
            "testCases": [
                {
                    "input": "",
                    "expectedOutput": "Welcome to Java Programming!\nThis is line 2\nProgramming is fun!"
                }
            ]
        }
    },
    "learn": {
        "learn-java-print": {
            "learnId": "learn-java-print",
            "content": "# Your First Java Program: Hello World!\n\n## Welcome to Java Programming!\nEvery programmer's journey begins with \"Hello World!\" - a simple program that displays text on the screen. This tradition helps you learn the basic structure of a programming language.\n\n## Java Program Structure\nEvery Java program needs these essential components:\n\n### 1. Class Declaration\n```java\npublic class HelloWorld {\n    // Your code goes here\n}\n```\n- `public class` - Creates a public class (accessible from anywhere)\n- `HelloWorld` - The name of your class (must match your filename)\n- `{ }` - Curly braces contain your class code\n\n### 2. Main Method\n```java\npublic static void main(String[] args) {\n    // Your program starts here\n}\n```\n- `public static void main` - The entry point where your program begins\n- `String[] args` - Allows command-line arguments (don't worry about this yet!)\n\n### 3. Print Statement\n```java\nSystem.out.println(\"Hello World!\");\n```\n- `System.out.println()` - Prints text to the console\n- `\"Hello World!\"` - The text to display (must be in double quotes)\n- `;` - Semicolon ends the statement (required in Java!)\n\n## Complete Hello World Program\n```java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World!\");\n    }\n}\n```\n\n## Important Notes\n- Java is **case-sensitive**: `System` ≠ `system`\n- Every statement must end with a semicolon `;`\n- Text must be in double quotes `\"\"`\n- The class name must match your filename\n\n## What Happens When You Run This?\n1. Java finds your `main` method\n2. It executes the `System.out.println()` statement\n3. \"Hello World!\" appears in the console\n4. The program ends\n\nCongratulations! You're now ready to write your first Java program! 🎉",
            "title": "Your First Java Program: Hello World!"
        },
        "learn-java-print-enhanced": {
            "learnId": "learn-java-print-enhanced",
            "content": "# Java Output Fundamentals\n\n## System.out.println()\nThe `System.out.println()` method is your gateway to displaying information in Java programs.\n\n### Basic Syntax\n```java\nSystem.out.println(\"Your message here\");\n```\n\n### Key Points\n- **System**: A built-in Java class that provides access to system resources\n- **out**: A static field representing the standard output stream\n- **println**: A method that prints text followed by a new line\n- **Double quotes**: Used to enclose text strings\n- **Semicolon**: Required to end the statement\n\n### Multiple Lines\nYou can print multiple lines by calling println() multiple times:\n```java\nSystem.out.println(\"First line\");\nSystem.out.println(\"Second line\");\nSystem.out.println(\"Third line\");\n```\n\n### Tips for Beginners\n1. Always use double quotes for text (strings)\n2. Don't forget the semicolon at the end\n3. Java is case-sensitive: `system.out.println()` won't work\n4. Each println() automatically adds a new line at the end",
            "title": "Java Output & Print Statements"
        },
        "learn-java-if-statements": {
            "learnId": "learn-java-if-statements",
            "content": "# Java Conditional Statements (if-else)\n\n## What are If Statements?\nIf statements allow your program to make decisions based on conditions. They execute different code blocks depending on whether a condition is true or false.\n\n## Basic If Statement\n```java\nif (condition) {\n    // Code to execute if condition is true\n}\n```\n\n## If-Else Statement\n```java\nif (condition) {\n    // Code if condition is true\n} else {\n    // Code if condition is false\n}\n```\n\n## If-Else If Chain\n```java\nif (condition1) {\n    // Code if condition1 is true\n} else if (condition2) {\n    // Code if condition2 is true\n} else {\n    // Code if all conditions are false\n}\n```\n\n## Common Operators\n- `>` greater than\n- `<` less than\n- `>=` greater than or equal to\n- `<=` less than or equal to\n- `==` equal to\n- `!=` not equal to\n\n## Example: Age Categories\n```java\nint age = 25;\nif (age >= 18) {\n    System.out.println(\"Adult\");\n} else {\n    System.out.println(\"Minor\");\n}\n```\n\n## Best Practices\n1. Always use braces {} even for single statements\n2. Check conditions from most specific to least specific\n3. Use meaningful variable names\n4. Keep conditions simple and readable",
            "title": "Java If Statements & Conditions"
        }
    }
}
