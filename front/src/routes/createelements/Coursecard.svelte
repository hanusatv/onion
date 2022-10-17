<script>
    export let header = "header";
    export let title = "title";
    export let body = "body";
</script>

<div class="card box">
    <h5 class="card-header">{header}</h5>
    <div class="card-body">
        <h5 class="card-title">{title}</h5>
        <p class="card-text">
            {body}
        </p>
        <button type="button" class="btn btn-danger btn-lg">something</button>
    </div>
</div>
