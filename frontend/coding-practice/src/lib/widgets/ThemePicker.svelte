<script lang="ts">
    import { themes, applyTheme, getCurrTheme } from "$lib/config/themes"
	import ThemePreview from "./ThemePreview.svelte";
    import { onMount, onDestroy } from 'svelte';

    let selectedTheme = $state(getCurrTheme());

    function selectTheme(theme: typeof themes[number]) {
        selectedTheme = theme;
        // applyTheme expects a Theme typed value; keep existing behavior
        applyTheme(theme as any);
    }

    function onKeyDownSelect(e: KeyboardEvent, theme: typeof themes[number]) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            selectTheme(theme);
        }
    }

    let containerEl: HTMLElement | null = null;

    function onWheel(e: WheelEvent) {
        if (!containerEl) return;

        // only hijack vertical wheel when horizontal overflow exists
        if (containerEl.scrollWidth > containerEl.clientWidth) {
            // convert vertical wheel delta to horizontal scroll
            const delta = e.deltaY;
            // some mice have large deltas; scale for smoother movement
            const scrollAmount = Math.sign(delta) * Math.min(Math.abs(delta), 100);
            containerEl.scrollBy({ left: scrollAmount, behavior: 'auto' });
            e.preventDefault();
        }
    }

    onMount(() => {
        if (!containerEl) return;
        containerEl.addEventListener('wheel', onWheel, { passive: false });
    });

    onDestroy(() => {
        if (!containerEl) return;
        containerEl.removeEventListener('wheel', onWheel as EventListener);
    });

</script>

<div bind:this={containerEl} class='container'>
    {#each themes as theme}
        <div
            role="button"
            tabindex="0"
            aria-pressed={selectedTheme === theme}
            class="theme-card {selectedTheme === theme ? 'selected' : ''}"
            onclick={() => selectTheme(theme)}
            onkeydown={(e: KeyboardEvent) => onKeyDownSelect(e, theme)}
        >
            <ThemePreview compact={true} theme={theme}/>
        </div>
    {/each}
</div>

<style>
    .container {
        padding: 5px;
        display: flex;
        flex-direction: row;
        gap: 8px;
        overflow-x: auto;
    }

    .theme-card {
        padding: 4px;
        border-radius: 8px;
        border: 2px solid transparent;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: border-color 120ms ease, box-shadow 120ms ease, transform 120ms ease;
        outline: none;
        background: transparent;
    }

    .theme-card:focus-visible {
        box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 10%, transparent);
    }

    .theme-card:hover {
        transform: translateY(-2px);
    }

    .theme-card.selected {
        border-color: var(--accent);
    }
</style>