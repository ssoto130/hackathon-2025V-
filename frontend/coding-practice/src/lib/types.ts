// data shapes for the API.

export interface ContentSet {
	type: 'contentSet';
	content: (Course | Learn)[];
}

export interface Course {
	type: 'course'
	courseId: string;
	courseName: string;
	description: string;
	questionSets: QuestionSet[];
}


export interface QuestionSet {
	type: 'questionSet'
	questionSetId: string;
	name: string;
	questions: QuestionDetails[];
}

export interface QuestionDetails {
	questionId: string;
	questionName: string;
	questionDifficulty: questionDifficulty;
}

export enum questionDifficulty {
	easy = 'Easy',
	medium = 'Medium',
	hard = 'Hard',
	impossible = 'Impossible'
}

export interface Question {
	type: 'question';
	questionId: string;
	questionDifficulty: questionDifficulty;
	questionName: string;
	questionDetails: string;
	answer: string;
	baseFiles: FileContent[];
	hints: string[];
	learn: Learn;
}

export interface Learn {
	type: 'learn'
	learnId: string;
	title: string; 
	content: string;
}

export interface FileContent {
	fileName: string;
	content: string;
	editable: boolean;
}

export interface SendSubmission {
	questionId: string;
	files: {
		fileName: string;
		content: string;
	}[];
}

export interface SubmitResults {
	input: string;
	result: string;
	expectedResult: string;
	passedTests: boolean;
	error: string | undefined;
}