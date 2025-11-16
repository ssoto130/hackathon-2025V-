<script lang="ts">
	import { page } from '$app/state';
</script>

<div class="error-container">
	<h1 class="error-status">{page.status}</h1>

	<p class="error-message">{page.error?.message}</p>

	<a href="/" class="home-link">Go to Homepage</a>
</div>

<style>
	.error-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 80vh;
		text-align: center;
	}

	.error-status {
		font-size: 10rem;
		font-weight: 700;
		color: var(--primary);
		margin: 0;
	}

	.error-message {
		font-size: 1.5rem;
		color: var(--muted);
		margin: 1rem 0;
	}

	.home-link {
		margin-top: 2rem;
		padding: 10px 20px;
		border-radius: var(--bigRound);
		background-color: var(--overlay);
		color: var(--text-color);
		text-decoration: none;
		transition: background-color 0.2s;
	}

	.home-link:hover {
		background-color: var(--border);
	}
</style>
