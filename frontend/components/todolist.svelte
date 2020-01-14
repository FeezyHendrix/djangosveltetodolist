<script>
    let todolists;
</script>

<div>
    {#each todolists as todolist}
        <div class="mt-2">
            <p>{todolist.title}</p>
            <p>{todolist.description}</p>
            <button class="btn btn-success mt-2">Select</button>
        </div>    
    {/each}
</div>