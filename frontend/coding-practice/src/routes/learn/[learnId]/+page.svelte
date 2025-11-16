<script lang="ts">
    import ContentRenderer from "$lib/frames/ContentRenderer.svelte";
	import { Gear, House } from 'phosphor-svelte';
    import type { Learn } from "$lib/types";
    import StyledButton from "$lib/components/StyledButton.svelte";
	import SettingsDialog from '$lib/widgets/SettingsDialog.svelte';

    const { data } = $props();

    const learnInfo: Learn = data.learnInfo;
</script>

<main>
    <div class='page-container'>
        <div>
            <a href="/">
                <StyledButton variant='icon'>
                    <House size={30} weight="fill" />
                </StyledButton>
            </a>
        </div>
        <div class='markdown-container'>
            <h1>{learnInfo.title}</h1>
            <ContentRenderer items={[learnInfo.content]}/>
        </div>
        <div>
            <SettingsDialog>
                {#snippet trigger()}
                    <StyledButton variant="icon">
                        <Gear size={30} weight="fill" />
                    </StyledButton>
                {/snippet}
            </SettingsDialog>
        </div>

    </div>
</main>

<style>
    main {
        padding: 1rem;
        height: 100%;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        overflow-y: auto;
        justify-content: center;
        align-items: center;
    }

	.page-container {
		flex: 1;
		display: flex;
		align-items: row;
		justify-content: space-between;
        width: 100%;
        height: 100%;
	}

    .markdown-container {
        width: 100%;
        max-width: 50rem;
        flex-grow: 1;
        padding: 20px;
        background-color: var(--surface);
        border-radius: var(--bigRound);
    }
    
    .markdown-container h1 {    
		text-align: center;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--border);
        width: 90%;
        margin-left: auto;
        margin-right: auto;
    }
</style>
