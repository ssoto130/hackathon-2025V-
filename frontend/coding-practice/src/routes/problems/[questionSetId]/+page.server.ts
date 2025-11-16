import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { QuestionSet, Question } from '$lib/types';

// gets the question set and the base question
export const load: PageServerLoad = async ({ params, fetch, url }) => {
    const questionSetResponse = await fetch(`/api/question-set/${params.questionSetId}`);
    
    if (!questionSetResponse.ok) {
        const errorData = await questionSetResponse.json();
        const message = errorData.message || `Failed to load question set: ${questionSetResponse.statusText}`;
        throw error(questionSetResponse.status, message);
    }

    const questionSet: QuestionSet = await questionSetResponse.json();

    // if the question array is empty
    if (!questionSet.questions || questionSet.questions.length === 0) {
        throw error(500, `API response for question set '${questionSet.name}' is missing a 'questions' array.`);
    }

    const urlQuestionId = url.searchParams.get('questionId');
    let defaultQuestionId: string | undefined;

    // use the questionId from the URL if it exists and is valid, otherwise fall back to the first question
    if (urlQuestionId && questionSet.questions.some(q => q.questionId === urlQuestionId)) {
        defaultQuestionId = urlQuestionId;
    } else {
        defaultQuestionId = questionSet.questions[0]?.questionId;
    }

    if (!defaultQuestionId) {
        throw error(500, `The question set '${questionSet.name}' contains no questions.`);
    }

    const defaultQuestionResponse = await fetch(`/api/question-details/${defaultQuestionId}`);
    if (!defaultQuestionResponse.ok) {
        throw error(defaultQuestionResponse.status, `Failed to load the default question: \n${defaultQuestionResponse.statusText}`);
    }

    const defaultQuestion: Question = await defaultQuestionResponse.json();

    return { questionSet, defaultQuestion };
};
