import { error, json } from '@sveltejs/kit';
import type { ContentSet } from '$lib/types';
import { API_URL } from '$lib/config/config';

// gets the course info
export async function GET() {
    try {
        const response = await fetch(`${API_URL}/base-content`);

        if (!response.ok) {
            throw error(response.status, `Couldn't load the content`);
        }

        const courses: ContentSet = await response.json();
        return json(courses);
    } catch(err) {
        throw error(502, 'Failed to fetch content')
    }

}