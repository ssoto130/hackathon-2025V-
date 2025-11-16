import { json, error, type RequestEvent } from '@sveltejs/kit';
import { API_URL } from '$lib/config/config';

// gets the question info from questionId
export async function GET(event: RequestEvent) {
    const questionId = event.params.questionId!;

    try {
        const response = await fetch(`${API_URL}/question-details/${questionId}`)

        if (response.status === 404) {
            throw error(404, `Question with ID '${questionId}' not found.`);
        }
        if (!response.ok) {
            throw error(response.status, `Backend returned status ${response.status}`);
        }

        const questionData = await response.json();
        
        return json(questionData);
    } catch (err) {
        throw error(502, `Failed to fetch question ${questionId} from backend`)
    }
    
}