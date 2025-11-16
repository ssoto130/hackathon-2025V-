<script lang="ts">
    import type { Snippet } from 'svelte';
	import { Dialog } from "bits-ui";
    import StyledButton from '$lib/components/StyledButton.svelte';

	let {
        title,
		children,
        trigger
	}: {
        title?: Snippet;
        trigger: Snippet;
		children: Snippet;
	} = $props();
</script>

<Dialog.Root>
	<Dialog.Trigger>
        {@render trigger()}
    </Dialog.Trigger>
	<Dialog.Portal>
        <Dialog.Overlay class='dialog-overlay'/>
		<Dialog.Content class='dialog-content'>
            {#if title}
                <Dialog.Title class='dialog-title'>
                    {@render title()}
                </Dialog.Title>
            {/if}
			<Dialog.Description class='dialog-description'>
                {@render children()}
            </Dialog.Description>
            <Dialog.Close class='dialog-close-btn'>
                <StyledButton variant='danger'> 
                    Close
                </StyledButton>
            </Dialog.Close>
		</Dialog.Content>
	</Dialog.Portal>
</Dialog.Root>

<style>
</style>