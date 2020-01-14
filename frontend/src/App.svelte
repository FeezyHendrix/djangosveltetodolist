<script>
	import { onMount } from 'svelte';


	export let todolist;
	const base_url = 'http://localhost:8000';

	onMount(async () => {
		fetchTodoList();
	});

	const fetchTodoList = async () => {
		const response = await fetch(`${base_url}/list`);	
		todolist = await response.json();
		console.log(todolist);
	}
</script>

<main>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>