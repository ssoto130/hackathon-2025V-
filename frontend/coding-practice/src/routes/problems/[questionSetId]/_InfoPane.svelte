<script lang="ts">
	import type { Learn } from '$lib/types';
	import ContentRenderer from '$lib/frames/ContentRenderer.svelte';
	import Tabs, { type TabItem } from '$lib/components/Tabs.svelte';
	import SpoilerButton from '$lib/components/SpoilerButton.svelte';
	import AiChat from '$lib/widgets/AiChat/AiChat.svelte';
	import type { ChatMessage, Context } from '$lib/widgets/AiChat/prompts';

	let {
		questionInfo,
		answer,
		learn,
		hints,
		context
	}: {
		questionInfo?: string;
		answer?: string;
		learn?: Learn;
		hints?: string[];
		context?: Context;
	} = $props();

	const tabItems: TabItem[] = [];
	if (questionInfo) tabItems.push({ id: 'question', title: 'Question' });
	if (answer) tabItems.push({ id: 'answer', title: 'Answer' });
	if (learn) tabItems.push({ id: 'learn', title: 'Learn' });
	if (hints) tabItems.push({ id: 'hints', title: 'Hints' });
	tabItems.push({ id: 'ai', title: 'AI' });

	let selectedInfoTab = $derived(tabItems[0].id);
	
	let chatMessages: ChatMessage[] = $state([]);

	let hintsShown = new Set<number>();
	function revealHint(i: number) {
		hintsShown.add(i);
	}
</script>

<div class="container">
	<Tabs items={tabItems} bind:value={selectedInfoTab}>
		{#if selectedInfoTab === 'question'}
			<div class="content-wrapper">
				<ContentRenderer items={[questionInfo!]} />
			</div>
		{:else if selectedInfoTab === 'learn'}
			<div class="content-wrapper">
				<ContentRenderer
					items={[`# ${learn?.title}\n`, `[Open Page](/learn/${learn?.learnId})`, learn?.content!]}
				/>
			</div>
		{:else if selectedInfoTab === 'answer'}
			<div class="content-wrapper">
			<ContentRenderer items={[answer!]} />
			</div>
		{:else if selectedInfoTab === 'hints'}
			<div class="content-wrapper">
				{#each hints as hint, i}
					<div class="hint-item">
						<SpoilerButton
							onClicked={() => {
								revealHint(i);
							}}
							hidden={!hintsShown.has(i)}
						>
							{#snippet hiddenItem()}
								{hint}
							{/snippet}
							{#snippet onTopItem()}
								hint {i}
							{/snippet}
						</SpoilerButton>
					</div>
				{/each}
			</div>
		{:else if selectedInfoTab === 'ai'}
			<!-- this part is outside the bigger if for layout reasons -->
			<div class="chat-container">
				<AiChat bind:chats={chatMessages} context={context}/>
			</div>
		{/if}
	</Tabs>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		height: 100%;
		width: 100%;
	}

	.content-wrapper {
		/* the flex part stops it from doing weird growing in height stuff */
		overflow-y: auto;
		padding: 8px 16px;
		scrollbar-gutter: stable;
	}

	.chat-container {
		height: 100%;
		overflow-y: hidden;
	}

	.hint-item {
		padding: 4px;
	}
</style>
