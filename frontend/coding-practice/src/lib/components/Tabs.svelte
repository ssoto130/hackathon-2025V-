<script lang="ts">
	import { Tabs } from 'bits-ui';
	import type { Snippet } from 'svelte';

	export type TabItem = {
		id: string;
		title: string;
	};

	let {
		items = [] as TabItem[],
		value = $bindable<string>(),
		children
	}: {
		items: TabItem[];
		value?: string;
		children: Snippet;
	} = $props();

	// select a default item if no value is provided
	if (!value && items.length > 0) {
		value = items[0].id;
	}
</script>

<Tabs.Root bind:value class="tabs-root">
	<Tabs.List class="tabs-list">
		{#each items as item (item.id)}
			<Tabs.Trigger class="tabs-trigger" value={item.id}>{item.title}</Tabs.Trigger>
		{/each}
	</Tabs.List>

	<div class="content-wrapper">
		{@render children()}
	</div>
</Tabs.Root>

<style>
	.content-wrapper {
		flex: 1 1 0;
		display: flex;
		flex-direction: column;
		overflow: auto;
	}
</style>