<script lang='ts'>
  // WARNING: when loading it has the primary color, it is meant to be the hover color of it's variant but to save time I am not implementing that due to not needing it
  import { Button } from 'bits-ui';
  import type { Snippet } from 'svelte';
	import { SpinnerGap } from 'phosphor-svelte';

  type Variant = 'base' | 'transparent' | 'primary' | 'secondary' | 'danger' | 'success' | 'warning' | 'icon' | 'disabled' | 'loading';

  let {
    variant = 'primary',
    children,
    onClicked,
    class: className,
    loading
  }: {
    variant?: Variant;
    children: Snippet,
    class?: string,
    onClicked?: () => void;
    loading?: boolean;
  } = $props();
</script>

<Button.Root
  onclick={onClicked}
  class={`styled-button ${className}`}
  data-variant={loading ? 'loading' : variant}
>

{#if loading}
  <div style:visibility='hidden'>
    {@render children()}
  </div>
  <SpinnerGap class='spinner styled-button-spinner' size={20} weight='bold'/>
{:else}
  {@render children()}
{/if}
</Button.Root>
