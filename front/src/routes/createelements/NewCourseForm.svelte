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
                    <select class="form-select form-select-lg mb-3">
                        <option selected>Semster</option>
                        <option value="1">One</option>
                        <option value="2">Two</option>
                        <option value="3">Three</option>
                    </select>
                    <!--Course Code like IKT100-->
                    <div class="form-floating mb-3">
                        <input
                            type="text"
                            class="form-control"
                            id="coursecode"
                            placeholder="IKT-100"
                        />
                        <label for="coursecode">Code</label>
                    </div>
                    <!--Name of course Grunnleggende programmering -->
                    <div class="form-floating mb-3">
                        <input
                            type="text"
                            class="form-control"
                            id="coursename"
                            placeholder="Grunnleggende Programmering"
                        />
                        <label for="coursename">Name</label>
                    </div>
                    <!--ECTS points 5, 7.5, 10-->
                    <div class="form-floating mb-3">
                        <input
                            type="text"
                            class="form-control"
                            id="ects"
                            placeholder="7.5"
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
                <button type="button" class="btn btn-primary">Save</button>
            </div>
        </div>
    </div>
</div>
