<script>
    import Courses from "./createelements/Courses.svelte";
    import Exams from "./createelements/Exams.svelte";

    var activetab = Courses;
</script>

<nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" on:click={() => (activetab = Courses)}
                        >Courses</a
                    >
                </li>
                <li class="nav-item">
                    <a class="nav-link" on:click={() => (activetab = Exams)}
                        >Exams</a
                    >
                </li>
            </ul>
        </div>
    </div>
</nav>
<main>
    <svelte:component this={activetab} />
</main>
