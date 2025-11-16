<script lang="ts">
	// TODO: save file content to cookies and load it too
	// TODO: when a panel is too small it messes with the sizes due to generating a a scrollbar and that pushing things
	
	// error popup when error, ensure you can easily escape the error by pressing enter and editor goes back to focus ig

	// QOL: the terminal starts off minimized until the run button is pressed

	import { Gear, House } from 'phosphor-svelte';
	import { Pane, Splitpanes } from 'svelte-splitpanes';
	import StyledButton from '$lib/components/StyledButton.svelte';
	import SettingsDialog from '$lib/widgets/SettingsDialog.svelte';
	import CodeEditor from '$lib/code_blocks/CodeEditor.svelte';
	import QuestionList from './_QuestionList.svelte';
	import TerminalPane from './_TerminalPane.svelte';
	import InfoPane from './_InfoPane.svelte';
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import type { QuestionSet, Question, FileContent, SendSubmission, SubmitResults } from '$lib/types';
	import { error } from '@sveltejs/kit';
	import Confetti from 'svelte-confetti';
	import { tick } from 'svelte';
	import type { Context } from '$lib/widgets/AiChat/prompts';

	const { data } = $props();
	const questionSet: QuestionSet = data.questionSet;
	let selectedQuestionId: string = $state(data.defaultQuestion.questionId);
	let questionInfo: Question = $state(data.defaultQuestion);
	let files: FileContent[] = $derived(questionInfo.baseFiles);

	let isSubmitting = $state(false);
	let submissionResults: SubmitResults | undefined = $state();

	let context: Context = $derived({
			currentCode: files,
			questionDetails: questionInfo.questionDetails,
			questionAnswer: questionInfo.answer,
			learnContent: questionInfo.learn.content,
			terminalOutput: submissionResults
		});

	$inspect(questionSet);
	
	// fetches new question details whenever a new id has been selected
	$effect(() => {
		async function fetchQuestionDetails() {
			if (!selectedQuestionId) {
				return;
			}

			const response = await fetch(`/api/question-details/${selectedQuestionId}`);

			if (!response.ok) {
				throw error(500, `error loading question details of ${selectedQuestionId}: ${response.text}` );
			}
			const currentUrl = new URL(page.url);
			if (currentUrl.searchParams.get('questionId') !== selectedQuestionId) {
				currentUrl.searchParams.set('questionId', selectedQuestionId);
				goto(currentUrl.toString(), { replaceState: true, noScroll: true });
			}
			
			questionInfo = await response.json();
			files = questionInfo.baseFiles;
		}
		fetchQuestionDetails();
	});
	
	async function onSubmit() {
		isSubmitting = true;
		const submissionInfo: SendSubmission = {
			questionId: selectedQuestionId,
			files: files
		}

		const response = await fetch('/api/submit', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(submissionInfo)
		});

		
		if (!response.ok) {
			throw error(500, `Error submitting question` );
		}

		submissionResults = await response.json();
		isSubmitting = false;
		
		if (submissionResults!.passedTests) {
			activateConfetti();
		}
	}
	
	let showConfetti = $state(false);
	async function activateConfetti() {
		showConfetti = false;
		await tick();
		showConfetti = true;
	}
</script>

<div class="page-container">
	<div class="top-bar">
		<div class="top-bar-section">
			<a href="/">
				<StyledButton variant='icon'>
					<House size={30} weight="fill" />
				</StyledButton>
			</a>
			<div class='vertical-seperator'></div>
			<QuestionList questionSet={questionSet} selectedQuestion={questionInfo} bind:selectedQuestionId/>
		</div>
		<div class="top-bar-section">
			<StyledButton variant="primary" onClicked={onSubmit} loading={isSubmitting}>RUN</StyledButton>
		</div>
		<div class="top-bar-section">
			<SettingsDialog>
				{#snippet trigger()}
					<StyledButton variant="icon">
						<Gear size={30} weight="fill" />
					</StyledButton>
				{/snippet}
			</SettingsDialog>
		</div>
	</div>
	<Splitpanes theme='splitpanes'>
		<Pane class='panel' size={25} minSize={15}>
			<InfoPane questionInfo={questionInfo.questionDetails} answer={questionInfo.answer} hints={questionInfo.hints} learn={questionInfo.learn} context={context}/>
		</Pane>
		<Pane minSize={15}>
    		<Splitpanes horizontal={true} theme='splitpanes'>
				<Pane class='panel' minSize={15}>
					<CodeEditor bind:files class="stretchy-editor" />
				</Pane>
				<Pane size={25} minSize={15}><TerminalPane loadingResult={isSubmitting} submitResults={submissionResults}/></Pane>
			</Splitpanes>
		</Pane>
	</Splitpanes>
	{#if showConfetti}
		<div class="confetti-overlay">
			<div class="confetti-container bottom-left">
				<Confetti cone amount={100} x={[0.5, 3]} y={[2, 4]} duration={3000} colorArray={['var(--primary)', 'var(--secondary)', 'var(--accent)', 'var(--success)']}/>
			</div>
			<div class="confetti-container bottom-right">
				<Confetti cone amount={100} x={[-0.5, -3]} y={[2, 4]} duration={3000} colorArray={['var(--primary)', 'var(--secondary)', 'var(--accent)', 'var(--success)']}/>
			</div>
		</div>
	{/if}
</div>

<style>
	.vertical-seperator {
		width: 1px;
		height: 30px;
		background-color: var(--border);
		gap: 4px;
	}

	.page-container {
		display: flex;
		flex-direction: column;
		height: 100vh;
		padding: 8px;
		gap: 8px;
	}
	
	.top-bar {
		display: flex;
		flex-shrink: 0;
		flex-direction: row;
		justify-content: space-between;
	}
	.top-bar-section {
		flex: 1;
		display: flex;
		align-items: center;
		gap: 3px;
	}

	.top-bar-section:nth-child(1) {
		justify-content: flex-start;
	}

	.top-bar-section:nth-child(2) {
		justify-content: center;
	}

	.top-bar-section:nth-child(3) {
		justify-content: flex-end;
	}

	.confetti-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100vw;
		height: 100vh;
		pointer-events: none;
		z-index: 9999;
	}

	.confetti-container {
		position: absolute;
	}

	.bottom-left {
		bottom: 0;
		left: 0;
	}

	.bottom-right {
		bottom: 0;
		right: 0;
	}
</style>
