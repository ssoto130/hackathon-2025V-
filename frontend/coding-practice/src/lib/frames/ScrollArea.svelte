<script lang="ts">
	import type { Snippet } from "svelte";
	import { ScrollArea } from "bits-ui";

	let {
		children,
		type = "hover", // 'always' | 'scroll' | 'hover' — Bits UI defaults
		className = ""
	}: {
		children: Snippet;
		type?: "always" | "scroll" | "hover";
		className?: string;
	} = $props();
</script>

<ScrollArea.Root type={type} class={`scroll-area-root ${className}`}>
	<ScrollArea.Viewport class="scroll-area-viewport">
		{@render children()}
	</ScrollArea.Viewport>

	<ScrollArea.Scrollbar orientation="vertical" class="scrollbar-vertical">
		<ScrollArea.Thumb class="scrollbar-thumb" />
	</ScrollArea.Scrollbar>

	<ScrollArea.Scrollbar orientation="horizontal" class="scrollbar-horizontal">
		<ScrollArea.Thumb class="scrollbar-thumb" />
	</ScrollArea.Scrollbar>

	<ScrollArea.Corner class="scrollbar-corner" />
</ScrollArea.Root>

<style>
</style>
