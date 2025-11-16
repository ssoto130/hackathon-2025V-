<script lang="ts">
	import { Checkbox, Label, useId } from 'bits-ui';
	import Check from 'phosphor-svelte/lib/Check';
	import Minus from 'phosphor-svelte/lib/Minus';

	let {
		label = 'Checkbox',
		checked = $bindable(false),
		indeterminate = $bindable(false),
		name,
		onCheck
	}: {
		label?: string;
		checked?: boolean;
		indeterminate?: boolean;
		name?: string;
		onCheck?: (checked: boolean) => void;
	} = $props();

    function onChecked(newChecked: boolean) {  
        if (indeterminate) {
            indeterminate = false;
            checked = true;
        } else {
            checked = newChecked;
        }

        onCheck?.(checked);
    }

	const id = useId();
</script>

<div class="container">
	<Checkbox.Root
		{id}
		bind:checked
		onCheckedChange={onChecked}
		bind:indeterminate
		{name}
		class="checkbox"
		aria-labelledby="{id}-label"
	>
		{#snippet children({ checked, indeterminate })}
			<div class="icon-wrap">
				{#if indeterminate}
					<Minus size={22} weight="bold" />
				{:else if checked}
					<Check size={22} weight="bold" />
				{/if}
			</div>
		{/snippet}
	</Checkbox.Root>

	<Label.Root id="{id}-label" for={id} class="label">
		{label}
	</Label.Root>
</div>

<style>
	.container {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		width: fit-content;
		height: fit-content;
	}

	:global(.checkbox) {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 22px;
		height: 22px;

		border-radius: var(--smallRound);
		border: 1px solid var(--border);
		background-color: var(--surface);
		cursor: pointer;

		transition: border 0.15s ease, background-color 0.15s ease, transform 0.1s ease;
	}

	:global(.checkbox:focus-visible) {
		outline: none;
		border: 1px solid var(--primary);
	}

	:global(.checkbox:hover) {
		border-color: var(--primary-40, var(--primary));
	}

	:global(.checkbox:active) {
		transform: scale(0.96);
	}
    :global(.checkbox[data-state='checked']) {
        border-width: 2px;
    }


	.icon-wrap {
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--primary);
	}

	:global(.label) {
		font-size: 0.95rem;
		cursor: pointer;
		user-select: none;
	}
</style>
