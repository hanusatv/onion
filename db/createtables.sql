-- SQLite
    BEGIN;
    CREATE TABLE semesters (
        semester_id NOT NULL PRIMARY KEY,
        code text NOT NULL,
        description text NOT NULL);


    CREATE TABLE courses (
        course_id text NOT NULL PRIMARY KEY,
        description text NOT NULL,
        semester integer,
        ECTS real,
        FOREIGN KEY (semester)
            REFERENCES semesters (course_id));

    CREATE TABLE exams (
        exam_id integer PRIMARY KEY AUTOINCREMENT,
        description text NOT NULL,
        course text NOT NULL,
        date text
    );

    COMMIT;