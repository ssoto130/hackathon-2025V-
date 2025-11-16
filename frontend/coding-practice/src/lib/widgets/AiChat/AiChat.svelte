<script lang="ts">
    import { PaperPlaneTilt, CircleNotch, Broom } from "phosphor-svelte";
    import StyledButton from "$lib/components/StyledButton.svelte";
    import SubmitApiKey from "./SubmitApiKey.svelte";
    import { apiKey, loadKey } from "../../config/apiKey.svelte";
	import { onMount, tick } from "svelte";
    import { GoogleGenAI } from "@google/genai";
    import { generateFullPrompt, type ChatMessage, type Context } from "./prompts";
    import ContentRenderer from '$lib/frames/ContentRenderer.svelte';
    import DropdownMenu from "$lib/components/DropdownMenu.svelte";

    let {
        context,
        chats = $bindable<ChatMessage[]>()
    }:{
        context?: Context; 
        chats?: ChatMessage[];
    } = $props();
    onMount(() => {
        loadKey();
    });

    
    const aiAgentOptions = [{ value: 'gemini-2.5-pro', label: 'Gemini 2.5 pro'}, { value: 'gemini-2.5-flash', label: 'Gemini 2.5 flash'}, { value: 'gemini-2.5-flash-lite', label: 'Gemini 2.5 lite'}];
    let aiAgent = $state('gemini-2.5-flash');
    let message = $state('');
    let gettingResponse = $state(false);
    let messagesContainer: HTMLDivElement;
    let textareaElement: HTMLTextAreaElement;

    async function sendMessage() {
        if (!message.trim()) return;
        gettingResponse = true;
        chats = [...chats, { role: 'user', content: message }];
        message = '';
        if (textareaElement) {
            textareaElement.style.height = 'auto';
        }
        await scrollToBottom();

        let content: string = generateFullPrompt(chats, context);

        try {
            const ai = new GoogleGenAI({
                apiKey: apiKey.key
            }); 
            const response = await ai.models.generateContent({
                model: aiAgent,
                contents: content
            })
            console.log(response.text);
            
            chats = [...chats, {role: 'ai', content: response.text ?? 'No Response...'}];
        } catch (e: any) {
            chats = [...chats, {role: 'ai', content: `Error: ${e.message ?? 'An unknown error occurred.'}`}];
        } finally {
            await scrollToBottom();
            gettingResponse = false;
        }
    }

    async function scrollToBottom() {
        await tick();
        if (messagesContainer) {
            messagesContainer.scrollTo({
                top: messagesContainer.scrollHeight,
                behavior: 'smooth'
            });
    }
    }

    function autoResize(e: Event) {
        const textarea = e.target as HTMLTextAreaElement;
        textarea.style.height = 'auto';
        const style = getComputedStyle(textarea);
        const lineHeight = parseFloat(style.lineHeight);
        const maxHeight = lineHeight * 10;

        let newHeight = textarea.scrollHeight;

        if (newHeight > maxHeight) {
            textarea.style.overflowY = 'scroll';
            newHeight = maxHeight;
        } else {
            textarea.style.overflowY = 'hidden';
        }
        textarea.style.height = `${newHeight}px`;
    }

    function clearMessages() {
        chats = [];
    }

</script>

{#if apiKey.key}
    <div class = 'chat-container'>
        <div class='messages' bind:this={messagesContainer}>
            {#each chats as chat, i (i)}
                <div class = 'message {chat.role}'>
                    <ContentRenderer items={[chat.content]}/>
                </div>
            {/each}
        </div>
        <div class='ai-interaction-area'>
            <div class='input-area'>
                <textarea
                    bind:this={textareaElement}
                    bind:value={message}
                    placeholder='Ask the ai a question...'
                    onkeydown={(e) => {
                        if (e.key === 'Enter' && !e.shiftKey) {
                            e.preventDefault();
                            sendMessage();
                        }
                    }}
                    oninput={autoResize}
                    rows='1'
                ></textarea>
                {#if gettingResponse}
                    <CircleNotch class='spinner' size={26} weight='bold'/>
                {:else}
                    <StyledButton variant='icon' onClicked={sendMessage}> <PaperPlaneTilt size={20} weight='fill'/></StyledButton>
                {/if}
            </div>
            <div class='option-area'>
                <DropdownMenu items={aiAgentOptions} bind:value={aiAgent}/>
                <StyledButton variant='icon' onClicked={clearMessages}> <Broom size={14} weight='fill'/></StyledButton>
            </div>
        </div>
    </div>
{:else}
<div class='api-enter-container'>
    <SubmitApiKey/>
</div>
{/if}

<style>
    .api-enter-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        justify-items: center;
        width: 100%;
        height: 100%;
        padding: 10px;
        gap: 2px;
    }


    .chat-container {
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
        overflow-x: hidden;		
    }

    .messages {
        flex: 1;
        overflow-y: auto;
        padding: 1rem;
        display: flex;
        flex-direction: column; 
        gap: 0.75rem;
    }

    .message {
        padding: 0rem 0.8rem;
        border-radius: var(--bigRound);
        max-width: 80%;
    }

    .message.user {
        background: var(--overlay);
        align-self: flex-end;
    }

    .message.ai {
        background: var(--overlay);
        border: 1px solid var(--primary);
        align-self: flex-start;
    }
    
    .ai-interaction-area {
        display: flex;
        flex-direction: column;
        margin-bottom: 5px;
        margin-left: 5px;
        margin-right: 5px;
        border: 1px solid var(--border);
        border-radius: var(--smallRound);
        padding: 8px;
    }
    .ai-interaction-area:focus-within {
        border: 1px solid var(--primary);
    }
    .input-area {
        display: flex;
        align-items: flex-end;
        border-bottom: 1px solid var(--border);
        padding-bottom: 4px;
    }
    .input-area textarea {
        background-color: transparent;
        border: none;
        flex: 1;
        resize: none;
        outline: none;
    }

    .input-area textarea:focus,
    .input-area textarea:focus-visible {
        outline: none; 
    }

    .option-area {
        display: flex;
        flex-direction: row;
        width: 100%;
        justify-content: space-between;
        padding-top: 5px;
    }
    :global(.select-content){
        margin-left: 13px;
    }
    :global(.select-trigger){
        font-size: 12px;
    }

    .api-setup {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        max-width: 400px;
        margin: 2rem auto;
        text-align: center;
    }
</style>