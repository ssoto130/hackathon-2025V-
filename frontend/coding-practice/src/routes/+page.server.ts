import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { ContentSet } from '$lib/types';

export const load: PageServerLoad = async ({ fetch }) => {

    const questionSetResponse = await fetch('/api/base-content');
    if (!questionSetResponse.ok) {
        const errorBody = await questionSetResponse.text();                              
        throw error(questionSetResponse.status, `Failed to fetch courses: ${errorBody}`);
    }

    const content: ContentSet = await questionSetResponse.json();
    return { content };
};