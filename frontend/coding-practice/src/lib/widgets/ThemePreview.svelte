<script lang="ts">
    import { browser } from '$app/environment';
    import { type Theme } from '$lib/config/themes';
    import { onMount } from 'svelte';

    // Use exported props so Svelte updates them normally.
	let {
		theme = 'light',
		compact = false,
	}: {
		theme: Theme;
        compact: boolean
	} = $props();

    // appliedTheme resolves the actual theme used for the preview.
    // If `theme` is `system`, use the user's OS preference when in the browser.
    let appliedTheme: string = $state('light');

    function updateAppliedTheme() {
        if (theme === 'system') {
            if (browser && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                appliedTheme = 'dark';
            } else {
                appliedTheme = 'light';
            }
        } else {
            appliedTheme = theme;
        }
    }

    onMount(() => {
        updateAppliedTheme();

        if (browser && window.matchMedia) {
            const mq = window.matchMedia('(prefers-color-scheme: dark)');
            const handler = () => updateAppliedTheme();

            mq.addEventListener('change', handler);

            return () => {
                mq.removeEventListener('change', handler);
            };
        }
    });

    // Ensure appliedTheme updates when `theme` prop changes.
    $effect(() => {
        updateAppliedTheme();
    });
</script>

<div class="theme-preview {compact ? 'compact' : ''}" data-theme={appliedTheme}>
    <div class="preview-window">
        <div class="window-header">
            <div class="window-controls">
                <div class="control-dot red"></div>
                <div class="control-dot yellow"></div>
                <div class="control-dot green"></div>
            </div>
            <div class="window-title">{theme}</div>
        </div>
        <div class="window-content">
            <div class="sidebar">
                <div class="nav-item primary"></div>
                <div class="nav-item secondary"></div>
                <div class="nav-item accent"></div>
            </div>
            <div class="main-content">
                <div class="content-header"></div>
                <div class="code-block">
                    <div class="code-line"></div>
                    <div class="code-line short"></div>
                    <div class="code-line"></div>
                    <div class="code-line medium"></div>
                </div>
                <div class="text-content">
                    <div class="text-line"></div>
                    <div class="text-line short"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .theme-preview {
        display: inline-block;
        padding: 0.5rem;
        border-radius: 0.5rem;
        background: var(--background, #ffffff);
    }
    
    .theme-preview.compact {
        padding: 0.25rem;
    }
    
    .preview-window {
        width: 200px;
        height: 120px;
        border-radius: 0.375rem;
        overflow: hidden;
        background: var(--background, #ffffff);
        border: 1px solid var(--border, #e5e7eb);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .window-header {
        height: 20px;
        background: var(--surface, #f8f9fa);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 8px;
        border-bottom: 1px solid var(--border, #e5e7eb);
    }
    
    .window-controls {
        display: flex;
        gap: 4px;
    }
    
    .control-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
    }
    
    .control-dot.red { background: var(--danger); }
    .control-dot.yellow { background: var(--warning); }
    .control-dot.green { background: var(--success); }
    
    .window-title {
        font-size: 0.6rem;
        color: var(--text-color, #6b7280);
        text-transform: capitalize;
    }
    
    .window-content {
        display: flex;
        height: calc(100% - 20px);
    }
    
    .sidebar {
        width: 40px;
        background: var(--surface, #f1f3f4);
        padding: 6px 4px;
        display: flex;
        flex-direction: column;
        gap: 3px;
    }
    
    .nav-item {
        height: 4px;
        background: var(--text-color, #9ca3af);
        border-radius: 2px;
    }
    
    .nav-item.primary {
        background: var(--primary, #3b82f6);
    }
    .nav-item.secondary {
        background: var(--secondary, #3b82f6);
    }
    .nav-item.accent {
        background: var(--accent, #3b82f6);
    }
    
    .main-content {
        flex: 1;
        padding: 6px;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    
    .content-header {
        height: 3px;
        background: var(--text-color, #374151);
        border-radius: 1.5px;
        width: 80%;
    }
    
    .code-block {
        background: var(--overlay, #f7f8f9);
        border-radius: 3px;
        padding: 4px;
        display: flex;
        flex-direction: column;
        gap: 2px;
        border: 1px solid var(--border, #e5e7eb);
    }
    
    .code-line {
        height: 2px;
        background: var(--text-color, #6366f1);
        border-radius: 1px;
    }
    
    .code-line.short { width: 60%; }
    .code-line.medium { width: 80%; }
    
    .text-content {
        display: flex;
        flex-direction: column;
        gap: 2px;
        margin-top: 2px;
    }
    
    .text-line {
        height: 2px;
        background: var(--secondary-text, #6b7280);
        border-radius: 1px;
    }
    
    .text-line.short { width: 70%; }
    
    .theme-preview.compact .preview-window {
        width: 160px;
        height: 96px;
    }
</style>