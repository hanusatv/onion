<script>
    const fetchSemesters = (async () => {
        const response = await fetch("http://localhost:8000/semesters");
        return await response.json();
    })();

    let semester, code, name, ects;

    async function submitSemester() {
        console.log("Rigar hetta?");
        fetch("http://localhost:8000/semesters/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                semester: semester,
                code: code,
                name: name,
                ects: ects,
            }),
        }).then(console.log("riggaði"));
    }
</script>

<!-- Modal -->
<div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">New Course</h5>
                <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                />
            </div>
            <div class="modal-body">
                <form>
                    <!--Semester 1,2,3... -->
                    <select
                        bind:value={semester}
                        class="form-select form-select-lg mb-3"
                    >
                        {#await fetchSemesters}
                            <p>...waiting</p>
                        {:then semesters}
                            <option value="">Semester</option>
                            {#each semesters.semesters as semester}
                                <option value={semester}
                                    >{semester.Description}</option
                                >
                            {/each}
                        {/await}
                    </select>
                    <!--Course Code like IKT100-->
                    <div class="form-floating mb-3">
                        <input
                            bind:value={code}
                            type="text"
                            class="form-control"
                            id="coursecode"
                            placeholder="IKT-100"
                            required
                        />
                        <label for="coursecode">Code</label>
                    </div>
                    <!--Name of course Grunnleggende programmering -->
                    <div class="form-floating mb-3">
                        <input
                            bind:value={name}
                            type="text"
                            class="form-control"
                            id="coursename"
                            placeholder="Grunnleggende Programmering"
                            required
                        />
                        <label for="coursename">Name</label>
                    </div>
                    <!--ECTS points 5, 7.5, 10-->
                    <div class="form-floating mb-3">
                        <input
                            bind:value={ects}
                            type="number"
                            class="form-control"
                            id="ects"
                            placeholder="7.5"
                            required
                        />
                        <label for="ects">ECTS</label>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button
                    type="button"
                    class="btn btn-secondary"
                    data-bs-dismiss="modal">Close</button
                >
                <button
                    on:click|preventDefault={submitSemester}
                    type="button"
                    class="btn btn-primary">Save</button
                >
            </div>
        </div>
    </div>
</div>
