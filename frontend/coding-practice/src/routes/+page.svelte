<script lang='ts'>
// TODO: when routing to the problems page, the kept courseId param breaks it, also pretty sure params here would break it so gotta account for those woop
// TODO: Change the base buttons to use StyledButton

import { onMount } from 'svelte';
import { page } from '$app/state';
import { goto } from '$app/navigation';
import type { Course, Learn, ContentSet } from '$lib/types';
import { Folder, Code, Note, Gear } from 'phosphor-svelte';
import StyledButton from '$lib/components/StyledButton.svelte';
import ContentRenderer from '$lib/frames/ContentRenderer.svelte';
import SettingsDialog from '$lib/widgets/SettingsDialog.svelte';

const { data } = $props();
let contentData = $state(data.content.content); // initial page data given from the +page.server.ts
let selectedId: string = $state('');
// updates the info when the course is changed
let selectedContent: (Course | Learn) = $derived.by(() => {
    for (let i = 0; i < contentData.length; i++) {
        const item = contentData[i];
        if ('courseName' in item && item.courseId === selectedId) {
            return item;
        } else if ('title' in item && item.learnId === selectedId){
            return item;
        }
    }
    return contentData[0];
});

$inspect(contentData);
// let weeks = $derived(selectedCourse?.weeks || []);

// load the default choice, from link params, cookies, default; priority is in that order.
onMount(() => {
    // url check
    const urlContentId = page.url.searchParams.get('contentId');
    if (urlContentId) {
        selectedId = urlContentId;
        return;
    }
    
    // local storage check
    const storedContentId = localStorage.getItem('contentId');
    if (storedContentId) {
        selectedId = storedContentId;
    }

    const firstContentItem = contentData[0];
    if ('courseName' in firstContentItem) {
        selectedId = firstContentItem.courseId;
    } else if ('title' in selectedContent) {
        selectedId = firstContentItem.learnId;
    }
});

// handles selectedCourseId changes (save to localStorage, update URL, fetches weeks)
// $effect(() => {
//     if (selectedId) {
//         // local storage
//         if (typeof window !== 'undefined') {
//             localStorage.setItem('courseId', selectedId);
//         }

//         // URL
//         const currentUrl = new URL(page.url);
//         if (currentUrl.searchParams.get('courseId') !== selectedId) {
//             currentUrl.searchParams.set('courseId', selectedId);
//             goto(currentUrl.toString(), { replaceState: true, noScroll: true });
//         }
//     } else {
//         // if selectedCourseId becomes undefined, remove from URL and localStorage
//         if (typeof window !== 'undefined') {
//             localStorage.removeItem('courseId');
//             const currentUrl = new URL(page.url);
//             if (currentUrl.searchParams.has('courseId')) {
//                 currentUrl.searchParams.delete('courseId');
//                 goto(currentUrl.toString(), { replaceState: true, noScroll: true });
//             }
//         }
//     }
// });
</script>

<main>
    <div class='content-selection-panel panel'>
        {#each contentData as content}
            {#if 'courseName' in content}
            <button onclick={() => {selectedId = content.courseId}}>
                <div 
                    class='content-selection-button' 
                    class:selected={selectedId === content.courseId}
                >
                    {content.courseName}
                    <Folder weight='fill' size='24px'/>
                </div>
            </button>
            {:else if 'title' in content}
            <button onclick={() => {selectedId = content.learnId}}>
                <div 
                    class='content-selection-button' 
                    class:selected={selectedId === content.learnId}
                >
                    {content.title}
                    <Note weight='fill' size='24px'/>
                </div>
            </button>
            {/if}
        {/each}
    </div>
    <div class='content-view'>
        {#if 'courseName' in selectedContent}
            <h1 class='content-title'>{selectedContent.courseName}</h1>
            <div class='inner-content'>
                {#each selectedContent.questionSets as questionSet}
                        <StyledButton onClicked={() => {
                            goto(`/problems/${questionSet.questionSetId}`);
                        }}>
                            <div class='content-button'>
                                <h3>
                                    {questionSet.name}
                                </h3>
                                <div>
                                    <Code size='30px' weight='bold'/>
                                </div>
                            </div>
                        </StyledButton>
                {/each}
            </div>
        {:else if 'title' in selectedContent}
            <h1 class='content-title'>{selectedContent.title}</h1>
            <div class='inner-content'>
                <ContentRenderer items={[selectedContent.content]} class='markdown-font'/>
            </div>
        {/if}
    </div>
    <div class='right-buttons'>
        <SettingsDialog>
            {#snippet trigger()}
                <StyledButton variant="icon">
                    <Gear size={32} weight="fill" />
                </StyledButton>
            {/snippet}
        </SettingsDialog>
    </div>
</main>

<style>
    main {
        display: flex;
        flex-direction: row;
        overflow-y: auto;
        height: 100%;
        width: 100%;
        padding: 1rem;
        gap: 8px;
    }

    .content-selection-panel {
        flex: 1;
        display: flex;
        flex-direction: column;
        line-height: 2.25rem;
        font-weight: 700;
        height: auto;
        padding: 0.5rem; 
        border-color: var(--border);
        background-color: var(--surface);
        gap: 5px;
        min-width: 400px;
        height: 100%;
    }
    
    .content-selection-button {
        padding: 3px 8px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        background-color: var(--overlay);
        border-radius: var(--bigRound);
        border: 1px solid var(--border);
    }

    .content-selection-button:hover {
        background-color: var(--highlight);
        cursor: pointer;
    }

    .content-selection-button.selected {
        border: 2px solid var(--primary);
        padding: 2px 7px;
    }
    .content-selection-button.selected:hover {
        background-color: var(--overlay);
    }

    .content-title {
        display: flex;
        flex-direction: row;
		text-align: center;
        justify-items: center;
        justify-content: center;
        margin-bottom: 0.5rem;
        border-bottom: 2px solid var(--border);
        width: 90%;
        margin-left: auto;
        margin-right: auto;
    }

    .content-view {
        flex: 3;
        display: flex;
        flex-direction: column;
        justify-content: start;
        gap: 4px;
        width: 100%;
    }

    .inner-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%;
        padding: 0px 8%;
        gap: 8px;
    }

    :global(.markdown-font) {
        font-size: 22px;
    }

    .content-button {
        width: 100%;
        justify-content: space-between;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    
    .right-buttons {
        display: flex;
        flex-direction: column;
    }
</style>