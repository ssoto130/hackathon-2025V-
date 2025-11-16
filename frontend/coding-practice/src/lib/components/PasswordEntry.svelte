<script lang="ts">
    import { Lock, LockOpen } from "phosphor-svelte";
    import StyledButton from "./StyledButton.svelte";

    let {
		value = $bindable<string>(),
        hintText = 'Input...',
        hidden = true,
        onSubmit
	}: {
		value?: string;
        hintText?: string;
        hidden?: boolean;
        onSubmit?: (value: string | undefined) => void;
	} = $props();

</script>

<div class="container">
    <input
        type={hidden ? 'password' : 'text'}
        placeholder={hintText}
        bind:value
        onkeydown={(e) => e.key === 'Enter' && onSubmit && onSubmit(value)}
    />
    <div class="visible-btn">
        <StyledButton variant="icon" onClicked={() => hidden = !hidden}>
            {#if hidden}
                <Lock size={20} weight={'fill'}/>
            {:else}
                <LockOpen size={20} />
            {/if}
        </StyledButton>
    </div>
</div>

<style>
    .container {
        display: flex;
        position: relative;
        flex-direction: row;
        width: 100%;
        height: fit-content;
        padding: 4px;
        border-radius: var(--smallRound);
        border: 1px solid var(--border);
        background-color: var(--surface);
    }    
    .container:focus-within {
        border: 1px solid var(--primary);
    }

    input {
        width: 100%;
        border: none;
        background-color: transparent;
    }
    .container input:focus,
    .container input:focus-visible {
        outline: none; 
        border-radius: calc(var(--smallRound) - 2px);
    }

    .visible-btn {
        align-items: center;
        display: flex;
    }

</style>