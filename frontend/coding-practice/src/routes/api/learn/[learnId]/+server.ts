import { json, error, type RequestEvent } from '@sveltejs/kit';
import { API_URL } from '$lib/config/config';

// gets the question info from questionId
export async function GET(event: RequestEvent) {
    const learnId = event.params.learnId!;

    try {
        const response = await fetch(`${API_URL}/learn/${learnId}`)

        if (response.status === 404) {
            throw error(404, `Learn info with id '${learnId}' not found.`);
        }
        if (!response.ok) {
            throw error(response.status, `Backend returned status ${response.status}\nWhen fetching the learn info with id ${learnId}`);
        }

        const learn = await response.json();
        
        return json(learn);
    } catch (err) {
        throw error(502, `Failed to learn info with id ${learnId} from backend`)
    }
}