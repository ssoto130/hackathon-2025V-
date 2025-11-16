<script lang="ts">
	import { Drawer } from "vaul-svelte";
    import type { Snippet } from 'svelte';

	let {
		children,
        trigger
	}: {
        trigger: Snippet;
		children: Snippet;
	} = $props();
</script>

<Drawer.Root direction='left'>
	<Drawer.Trigger>
        {@render trigger()}
    </Drawer.Trigger>
	<Drawer.Portal>
        <Drawer.Overlay class='left-drawer-overlay'/>
		<Drawer.Content class='left-drawer-content'>
			{@render children()}
		</Drawer.Content>
	</Drawer.Portal>
</Drawer.Root>