// dummy data for used by the +page.server.ts for testing and making purposes, will be replaced by actual server someday tm

// data shapes
import {
	type Course,
	type QuestionSet,
	type DatabaseQuestion,
	type Learn,
	questionDifficulty
} from '$lib/types';

// fake db, structure is flat table with id's pointing everywhere instead of nested
export const FAKE_DB = {
	courses: [
		{
			courseId: 'course1',
			courseName: 'programming fundamentals 1',
			description: 'start learning java woop',
			weeks: [
				{
					weekName: 'Week 1: printing to the console',
					questionSetId: 'qs1'
				},
				{
					weekName: 'Week 2: If statements',
					questionSetId: 'qs2'
				}
			]
		},
		{
			courseId: 'course2',
			courseName: 'programming fundamentals 2',
			description: 'Start getting into java OOP',
			weeks: [
				{
					weekName: 'Week 1: Java classes',
					questionSetId: 'qs3'
				}
			]
		}
	] as Course[],

	questionSets: {
		qs1: {
			questionSetId: 'qs1',
			name: 'Week 1 practice',
			questions: [
				{
					questionId: 'q1',
					questionName: 'hello world',
					questionDifficulty: questionDifficulty.easy
				},
				{
					questionId: 'q2',
					questionName: 'adding 2 vars',
					questionDifficulty: questionDifficulty.medium
				}
			]
		},
		qs2: {
			questionSetId: 'qs2',
			name: 'this is a question thingy',
			questions: [
				{
					questionId: 'q1',
					questionName: 'print statement',
					questionDifficulty: questionDifficulty.easy
				},
				{
					questionId: 'q1',
					questionName: 'if statement thing',
					questionDifficulty: questionDifficulty.medium
				},
				{
					questionId: 'q1',
					questionName: 'more questiopn testing',
					questionDifficulty: questionDifficulty.hard
				},
				{
					questionId: 'q1',
					questionName: 'last test',
					questionDifficulty: questionDifficulty.impossible
				},
				{
					questionId: 'q1',
					questionName: 'print statement',
					questionDifficulty: questionDifficulty.easy
				},
				{
					questionId: 'q2',
					questionName: 'if statement thing',
					questionDifficulty: questionDifficulty.medium
				},
				{
					questionId: 'q2',
					questionName: 'more questiopn testing',
					questionDifficulty: questionDifficulty.hard
				},
				{
					questionId: 'q2',
					questionName: 'last test',
					questionDifficulty: questionDifficulty.impossible
				}
			]
		}
	} as Record<string, QuestionSet>,

	questions: {
		q1: {
			questionId: 'q1',
			questionDifficulty: questionDifficulty.easy,
			questionName: 'hello world',
			questionDetails: 'write a program that prints hello world to the console',
			answer: 'System.out.println("hello world"); you\'d also add explanation here',
			baseFiles: [
				{
					fileName: 'LearnPrint.java',
					content: '// Write your code here also add the base class and main method',
					editable: true
				}
			],
			hints: ['you will use System.out.println();'],
			learnId: 'learn-java-print',
			testCases: [
				{
					input: '',
					expectedOutput: 'hello world'
				}
			]
		},
		q2: {
			questionId: 'q2',
			questionDifficulty: questionDifficulty.medium,
			questionName: 'adding 2 vars',
			questionDetails: 'write a program that adds 2 variables',
			answer: "System.out.println(2 + 2);\nyou'd also add explanation here",
			baseFiles: [
				{
					fileName: 'var_adding.java',
					content: 'print(aaa)',
					editable: true
				},
				{
					fileName: 'second_test_file.txt',
					content: 'idk it is just for testing',
					editable: false
				}
			],
			hints: ['you will use System.out.println();'],
			learnId: 'learn-java-print',
			testCases: [
				{
					input: '1\n2',
					expectedOutput: '3'
				},
				{
					input: '3\n5',
					expectedOutput: '8'
				}
			]
		}
	} as Record<string, DatabaseQuestion>,

	learn: {
		'learn-java-print': {
			learnId: 'learn-java-print',
			content: 'The `System.out.println()` method in Java is used to display output to the console.',
			title: 'Learn Java Print'
		}
	} as Record<string, Learn>
};

export const FAKE_LATENCY = 200; // milliseconds, 0.2 second delay
