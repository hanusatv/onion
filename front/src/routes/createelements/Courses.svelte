<script>
    import NewCourseForm from "./NewCourseForm.svelte";

    var modalNewCourse = false;
</script>

<div class="flex-container">
    <button
        data-bs-toggle="modal"
        data-bs-target="#staticBackdrop"
        type="button"
        class="btn btn-danger btn-lg"
        on:click={() => (modalNewCourse = !modalNewCourse)}>New</button
    >
    <button type="button" class="btn btn-danger btn-lg">Edit</button>
    <button type="button" class="btn btn-danger btn-lg">Delete</button>
</div>
<NewCourseForm />

<style>
    .flex-container {
        display: flex;
        justify-content: center;
        gap: 1em;
        margin-top: 2em;
    }
</style>
