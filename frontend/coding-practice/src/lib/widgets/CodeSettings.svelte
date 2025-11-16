<script lang="ts">
    import ComboBox from "$lib/components/ComboBox.svelte";
	import { updateFont, terminalSettings } from "$lib/config/terminalSettings.svelte";
    
    const fontOptions = [{ value: 'SUSE Mono', label: 'SUSE Mono' }, { value: 'Source Code Pro', label: 'Source Code Pro' }, { value: 'monospace', label: 'monospace' }]
    let chosenFont: string = $state(terminalSettings.font);
    const fontSizeOptions = [{value: '8', label: `8`}];
    for (let i = 10; i < 32; i+=2) {
        fontSizeOptions.push({value: `${i}`, label: `${i}`});
    }
    let chosenFontSize = $state(terminalSettings.fontSize.toString());
    $effect(() => {
        updateFont(chosenFont, +chosenFontSize);
    });
</script>

<div class='container'>
    <ComboBox items={fontOptions} bind:value={chosenFont} type='single' placeholder={`Font: ${chosenFont}`}/>
    <ComboBox items={fontSizeOptions} bind:value={chosenFontSize} type='single' placeholder={`Font size: ${chosenFontSize}`}/>
</div>

<style>
    .container {
        display: flex;
        align-items: center;
        gap: 4px;
    }
</style>