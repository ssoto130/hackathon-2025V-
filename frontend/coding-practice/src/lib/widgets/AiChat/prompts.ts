import type { FileContent, SubmitResults } from "$lib/types";

export const aiHelpPrompt: string = `[INSTRUCTIONS]
You are an ai helping out a student who is taking a computer programming course.
They are solving coding problems to help them get better.
Your goal is to help the student, you will be given the programming question, answer, what they learned for the week, their current code, previous terminal output if available and previous chat message if they exist.
Using this information you will prove help, hints and nudge them in the right direction, you will NOT under ANY circumstance give the student the answer, they must figure it out on their own.
Keep your messages relatively short, avoid overloading them with information and use markdown, focus.
Focus on giving more visual responses rather than long blocks of text, things such as lists, arrows, steps, and code blocks.
[/INSTRUCTIONS]`;

export const chatRoles = ['ai', 'user'] as const;
export type ChatRole = (typeof chatRoles)[number];
export interface ChatMessage {
    role: ChatRole;
    content: string;
};

export function generateMessagePrompt(messages: ChatMessage[]) {
    if (!messages) return '';
    let messagePrompt: string = '[CHAT HISTORY]';
    for (let i = 0; i < messages.length; i++) {
        const chat = messages[i];
        if (chat.role === 'ai') messagePrompt += 'Agent:\n';
        else messagePrompt += 'Student:\n';
        messagePrompt += `${chat.content}\n\n`;
    }
    messagePrompt += '[/CHAT HISTORY]';
    return messagePrompt;
}

export interface Context {
    questionDetails?: string;
    questionAnswer?: string;
    learnContent?: string;
    terminalOutput?: SubmitResults;
    currentCode?: FileContent[];
}

export function generateContextPrompt(context: Context) {
    const lines: string[] = ['[CONTEXT]'];

    if (context.questionDetails) lines.push(`Question details:\n${context.questionDetails}`);
    if (context.questionAnswer) lines.push(`Question answer:\n${context.questionAnswer}`);
    if (context.learnContent) lines.push(`Learn content:\n${context.learnContent}`);
    if (context.terminalOutput) {
        lines.push('Submission results:')
        lines.push(`Terminal input:\n${context.terminalOutput.input}`);
        lines.push(`Terminal output:\n${context.terminalOutput.result}`);
        lines.push(`Expected result:\n${context.terminalOutput.expectedResult}`);
    }
    if (context.currentCode) {
        lines.push('Current code:');
        context.currentCode.forEach(fileInfo => {
            lines.push(`${fileInfo.fileName}`);
            lines.push(`Student editable - ${fileInfo.editable}`);
            lines.push(`Content\n${fileInfo.content}`);
        });
    }

    lines.push('[/CONTEXT]');
    return lines.join('\n');
}

export function generateFullPrompt(messages: ChatMessage[], context?: Context) {
    let fullPrompt: string = aiHelpPrompt;
    if (context) {
        fullPrompt += generateContextPrompt(context);
    }
    if (messages) {
        fullPrompt += generateMessagePrompt(messages);
    }
    console.log(fullPrompt);
    return fullPrompt;
}