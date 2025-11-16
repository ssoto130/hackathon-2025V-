<script lang="ts">
	// TODO: add a scrollbar for the file list if it gets too large
	import BaseCodeEditor from '$lib/code_blocks/BaseCodeEditor.svelte';
	import Tabs from '$lib/components/Tabs.svelte';
	import { type FileContent } from '$lib/types';

    let { files = $bindable<FileContent[]>([]), class: className = '' } = $props();
    if (!files) { // ensures there is at least one file in the files
        files = [{
            fileName: 'untitled.txt',
            Content: 'There is no base files',
            editable: true
        }]
    }

    // if the files change these update
	const tabOptions = $derived(files.map((f) => ({ id: f.fileName, title: f.fileName })));
	let activeTabId = $derived(files[0].fileName);
	let code = $derived(files[0].content);   

    // changes the code to be the one in the specified file
    $effect(() => {
        code = files.find((f) => f.fileName === activeTabId)?.content ?? 'error loading code';
    });
    
    // updates the parent file list content
    $effect(() => {
        const activeFile = files.find((f) => f.fileName === activeTabId);
        if (activeFile && activeFile.content !== code) {
            activeFile.content = code;
        }
    });

    // updates and manages the file extension stuff
	let activeFileExtention = $derived(activeTabId?.split('.').pop() || '');
</script>

{#if files && files.length > 0}
	<div class="wrapper {className}">
		<Tabs items={tabOptions} bind:value={activeTabId}>
			<BaseCodeEditor 
                className="editor {className}" 
                bind:value={code} 
                language={activeFileExtention}
			/>
		</Tabs>
	</div>
{/if}

<style>
	.wrapper {
		display: flex;
		flex-direction: column;
		height: 100%;
		width: 100%;
	}
	.editor {
		flex: 1;
	}
</style>
