<script lang='ts'>
    import PasswordEntry from "$lib/components/PasswordEntry.svelte";
    import Checkbox from "$lib/components/Checkbox.svelte";
    import StyledButton from "$lib/components/StyledButton.svelte";
    import { apiKey, loadKey, updateKey } from "../../config/apiKey.svelte";
	import { onMount } from "svelte";

    onMount(() => {
        loadKey();
    });

    let inputKey = $state(apiKey.key);
    let saveToCookies = $state(false);

    function onSubmit() {
        updateKey(inputKey, saveToCookies);
    }
</script>

<div class="container">
    <PasswordEntry hintText={'Gemini api key'} bind:value={inputKey}/>
    <StyledButton onClicked={onSubmit}>Submit</StyledButton>
    <div class='save-container'>
        <Checkbox label='Save to cookies' bind:checked={saveToCookies}/>
    </div>
</div>

<style>
    .save-container {
        display: flex;
        padding: 5px 0px;
        gap: 4px;

}

    .container {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
</style>
