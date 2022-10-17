<script>
    import Coursecard from "./Coursecard.svelte";
    import NewCourseForm from "./NewCourseForm.svelte";

    const fetchCourses = (async () => {
        const response = await fetch("http://localhost:8000/courses");
        return await response.json();
    })();

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

<div class="d-flex flex-row mb-3">
    {#await fetchCourses}
        <p>...waiting</p>
    {:then courses}
        {#each courses.courses as course}
            <Coursecard header={course.course_id} title={course.description} />
        {/each}
    {:catch error}
        <p>An error occurred!</p>
    {/await}
</div>

<style>
    .flex-container {
        display: flex;
        justify-content: center;
        gap: 1em;
        margin-top: 2em;
    }
</style>
