<script>
    import { Select } from "bits-ui";
    import CaretDown from "phosphor-svelte/lib/CaretDown";

    let {
        items = [],
        value = $bindable(), 
        placeholder = "Select an option"
    } = $props();
    // idk how to make it type safe i gave up
    // {
    //     items: { value: string, label: string}[];
    //     value: string;
    //     placeholder: string;
    // }

    const selectedLabel = $derived(
        items.find(item => item.value === value)?.label ?? placeholder
    );
</script>

<Select.Root type='single' {items} bind:value>
    <Select.Trigger class='select-trigger'>
        <span>{selectedLabel}</span>
        <CaretDown class="size-4" weight='fill'/>
    </Select.Trigger>
    <Select.Portal>
        <Select.Content class='select-content'>
            <Select.Viewport>
                {#each items as c}
                    <Select.Item class='select-item' value={c.value} label={c.label} disabled={c.disabled}>
                        {#snippet children({ selected })}
                            <span>{c.label}</span>
                        {/snippet}
                    </Select.Item>
                {/each}
            </Select.Viewport>
        </Select.Content>
    </Select.Portal>
</Select.Root>