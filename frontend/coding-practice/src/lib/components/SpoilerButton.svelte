<script lang="ts">
	import type { Snippet } from 'svelte';
	import { fade } from 'svelte/transition';

	let {
		hidden = true,
		hiddenItem,
		onTopItem,
		onClicked
	}: {
		hidden?: boolean,
		hiddenItem: Snippet,
		onTopItem: Snippet,
    	onClicked?: () => void
	} = $props();

	let covering = $state(hidden);

	function reveal() {
		if (onClicked) onClicked();
		covering = false;
	}
</script>

<div class="reveal-container">
	<!-- Hidden content is always rendered -->
	<div class="revealed-content" class:visible={!covering} transition:fade={{ duration: 400 }}>
		{@render hiddenItem()}
	</div>

	{#if covering}
		<button class="reveal-button" onclick={reveal} transition:fade={{ duration: 300 }}>
			{@render onTopItem()}
		</button>
	{/if}
</div>

<style>
	.reveal-container {
		position: relative;
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

.reveal-button {
	position: absolute; 
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	padding: 6px 12px;
	background-color: var(--muted);
	color: var(--text-color);
	border: none;
	border-radius: var(--smallRound);
	cursor: pointer;
}

	.reveal-button:hover {
		background-color: var(--primary);
	}

	.revealed-content {
		padding: 8px;
		background-color: var(--overlay);
		border-radius: 4px;
		opacity: 0;
		transition: opacity 0.3s ease;
		position: relative;
	}

	.revealed-content.visible {
		opacity: 1;
	}
</style>
