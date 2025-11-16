<script lang="ts">
	import { Combobox, type WithoutChildrenOrChild, mergeProps } from 'bits-ui';
	import { CaretUpDown, Placeholder } from 'phosphor-svelte';
	// TODO: default value shown and add the caretUpDown
	type Props = Combobox.RootProps & {
		inputProps?: WithoutChildrenOrChild<Combobox.InputProps>;
		contentProps?: WithoutChildrenOrChild<Combobox.ContentProps>;
		placeholder?: string;
	};

	let {
		items = [],
		value = $bindable(),
		open = $bindable(false),
		placeholder = typeof value === 'string' ? value : '',
		inputProps,
		contentProps,
		type,
		...restProps
	}: Props = $props();

	let searchValue = $state('');

	const filteredItems = $derived.by(() => {
		if (searchValue === '') return items;
		return items.filter((item) => item.label.toLowerCase().includes(searchValue.toLowerCase()));
	});

	function handleInput(e: Event & { currentTarget: HTMLInputElement }) {
		searchValue = e.currentTarget.value;
	}

	function handleOpenChange(newOpen: boolean) {
		if (!newOpen) {
			searchValue = items.find((item) => item.value === value)?.label ?? '';
		}
	}
	const mergedRootProps = $derived(mergeProps(restProps, { onOpenChange: handleOpenChange }));
	const mergedInputProps = $derived(
		mergeProps(inputProps, {
			oninput: handleInput,
			class: 'combobox-input',
			onclick: () => (open = true),
			Placeholder: placeholder
		})
	);
</script>

<Combobox.Root {type} {items} bind:value={value as never} bind:open {...mergedRootProps}>
	<Combobox.Input {...mergedInputProps} />
	<Combobox.Trigger class="combobox-trigger">
		
	</Combobox.Trigger>
	<Combobox.Portal>
		<Combobox.Content {...contentProps} class="combobox-content">
			{#each filteredItems as item, i (i + item.value)}
				<Combobox.Item {...item} class="combobox-item">
					{#snippet children()}
						{item.label}
					{/snippet}
				</Combobox.Item>
			{/each}
		</Combobox.Content>
	</Combobox.Portal>
</Combobox.Root>
