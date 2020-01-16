<script>
	import { onMount } from 'svelte';
	import TodoList from './components/todolist.svelte';


	export let todolist;
	const base_url = 'http://localhost:8000';

	onMount(async () => {
		fetchTodoList();
	});

	const fetchTodoList = async () => {
		try {
			const response = await fetch(`${base_url}/list`, { headers: { "Accept": "application/json",
        "Content-Type": "application/json" }});	
			todolist = await response.json();
			console.log(todolist);
		} catch(e) {
			console.log(e);
		}
	}
</script>

<main>
	{#if todolist}
		<div class="row">
			<div class="col-md-4">
				<TodoList todolist={todolist}> </TodoList>
			</div>
		</div>
	{:else} 
		<p>Loading</p>
	{/if }
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