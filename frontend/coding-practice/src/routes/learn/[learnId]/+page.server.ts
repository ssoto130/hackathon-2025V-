import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { Learn } from '$lib/types';

// gets the question set and the base question
export const load: PageServerLoad = async ({ params, fetch, url }) => {
    const learnResponse = await fetch(`/api/learn/${params.learnId}`);
    
    if (!learnResponse.ok) {
        const errorData = await learnResponse.json();
        const message = errorData.message || `Failed to load question set: ${learnResponse.statusText}`;
        throw error(learnResponse.status, message);
    }

    const learnInfo: Learn = await learnResponse.json();
    
    return { learnInfo };
};
