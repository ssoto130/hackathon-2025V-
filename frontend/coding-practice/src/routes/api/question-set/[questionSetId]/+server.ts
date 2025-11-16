import { error, json, type RequestEvent } from '@sveltejs/kit';
import { API_URL } from '$lib/config/config';

export async function GET(event: RequestEvent) {
    const questionSetId = event.params.questionSetId!;

    try {
        const response = await fetch(`${API_URL}/question-set/${questionSetId}`)

        if (response.status === 404) {
            throw error(404, `Question set with ID '${questionSetId}' not found.`);
        }
        if (!response.ok) {
            throw error(response.status, `Backend returned status ${response.status}\nWhen fetching question set with id ${questionSetId}`);
        }

        const questionSetData = await response.json();
        
        return json(questionSetData);
    } catch (err) {
        throw error(502, `Failed to fetch question set ${questionSetId} from backend`)
    }
}
