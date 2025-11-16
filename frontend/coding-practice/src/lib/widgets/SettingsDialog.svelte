<script lang="ts">
    import { type Snippet } from 'svelte';
    import Dialog from '$lib/frames/Dialog.svelte';
    import { themes, getCurrTheme, applyTheme, type Theme } from '$lib/config/themes';
    import ThemePicker from './ThemePicker.svelte';
    import SubmitApiKey from './AiChat/SubmitApiKey.svelte';
	import CodeSettings from './CodeSettings.svelte';
    
    const themeOptions = themes.map(item => ({
        label: item,
        value: item
    }));

    let currTheme: Theme = $state(getCurrTheme())

    $effect(()  => {
        applyTheme(currTheme);
    });

    let {
        trigger: _trigger
	}: {
        trigger: Snippet;
	} = $props();
</script>

<Dialog trigger={_trigger}>
    {#snippet title()}
        <h1>Settings</h1>
    {/snippet}
    <div class="settings-content">
        <div class="setting-group">
            <div class="hint-text">Theme</div>
            <ThemePicker/>
        </div>
        <div class="setting-group">
            <div class='hint-text'>Code editor</div>
            <CodeSettings/>
        </div>
        <div class="setting-group">
            <div class='hint-text'>Api</div>
            <SubmitApiKey/>
        </div>
    </div>
</Dialog>

<style>
    .settings-content {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        padding: 1rem 0;
        max-width: 60vh;
    }
    
    .setting-group {
        display: flex;
        flex-direction: column;
    }
    
</style>
