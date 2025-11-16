import { error, json, type RequestEvent } from '@sveltejs/kit';
import type { SendSubmission, SubmitResults } from '$lib/types';
import { API_URL } from '$lib/config/config';


export async function POST({ request }: RequestEvent) {
    const submission: SendSubmission = await request.json();

    try {
        const response = await fetch(`${API_URL}/submit`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(submission)
        });

        if (!response.ok) {
            throw error(response.status, `Failed to run your submission`);
        }

        const data: SubmitResults = await response.json();
        return json(data);
    } catch (err) {
        throw error(502, 'Failed to reach the backend to run your submission');
    }
}
