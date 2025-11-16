<script lang="ts">
  import { marked } from 'marked';
  import BaseCodeEditor from '$lib/code_blocks/BaseCodeEditor.svelte';
  import { mount, onMount } from 'svelte';

  // only strings and svelte components
  let {
    items,
    class: className,
  }:{
    items: (string | (new (...args: any) => any))[]; 
    class?: string,
  } = $props();

  const renderer = new marked.Renderer();

  renderer.code = ({ text, lang }) => {
    const language = (lang || 'plaintext').trim();
    // encodeURIComponent ensures we don’t break attributes
    return `<div class="code-block" data-lang="${language}" data-code="${encodeURIComponent(text)}"></div>`;
  };

  marked.use({ renderer });

  let element: HTMLElement;

  // --- Hydrate those placeholders into real Svelte components ---
  $effect(() => {
    if (!element) return;
    element.querySelectorAll('.code-block').forEach((el) => {
      if (el.firstChild) return; // already mounted

      const language = el.getAttribute('data-lang') ?? 'plaintext';
      const code = decodeURIComponent(el.getAttribute('data-code') ?? '');

      mount(BaseCodeEditor, {
        target: el,
        props: { language, value: code, editable: false, className:'markdown-code-block' },
      });
    });
  });
</script>

<!-- Render Markdown or components -->
<div class={`markdown ${className}`} bind:this={element}>
  {#each items as item}
    {#if typeof item === 'string'}
      {@html marked(item)}
    {:else}
      {@const Component = item}
      <Component/>
    {/if}
  {/each}
</div>
