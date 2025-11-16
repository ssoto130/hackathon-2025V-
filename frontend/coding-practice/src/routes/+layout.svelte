<script lang="ts">
	import '../styles/app.css';
	import { onMount } from 'svelte';
	import { applyTheme, type Theme } from '$lib/config/themes';

	let { children } = $props();


	onMount(() => {
		const savedTheme = localStorage.getItem('data-theme') as Theme | null;
		applyTheme(savedTheme ?? 'system');
	});
</script>


{@render children?.()}
