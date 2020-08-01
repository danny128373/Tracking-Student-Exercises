DROP TABLE IF EXISTS cohorts;

DROP TABLE IF EXISTS exercises;

DROP TABLE IF EXISTS instructors;

DROP TABLE IF EXISTS students;

CREATE TABLE cohorts
(
    cohortId INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE exercises
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    language TEXT NOT NULL
);

CREATE TABLE instructors
(
    id INTEGER NOT NULL PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    slack TEXT NOT NULL,
    specialty TEXT NOT NULL,
    cohortId INTEGER NOT NULL,
    FOREIGN KEY (cohortId) REFERENCES cohorts(id)
);

CREATE TABLE students
(
    id INTEGER NOT NULL PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    slack TEXT NOT NULL,
    cohortId INTEGER NOT NULL,
    FOREIGN KEY (cohortId) REFERENCES cohorts(id)
);

CREATE TABLE studentExercises
(
    id INTEGER NOT NULL PRIMARY KEY,
    studentId INTEGER NOT NULL,
    exerciseId INTEGER NOT NULL,
    FOREIGN KEY(studentId) REFERENCES students(id),
    FOREIGN KEY(exerciseId) REFERENCES exercises(id)
);

-- CREATE 3 COHORTS
INSERT into cohorts
VALUES
    (NULL, 'Cohort 40');

INSERT into cohorts
VALUES
    (NULL, 'Cohort 41');

INSERT into cohorts
VALUES
    (NULL, 'Cohort 42');

-- CREATE 5 EXERCISES
INSERT into exercises
VALUES
    (NULL, 'Coins to Cash', 'Python');

INSERT into exercises
VALUES
    (NULL, 'War', 'Python');

INSERT into exercises
VALUES
    (NULL, 'FizzBuzz', 'JavaScript');

INSERT into exercises
VALUES
    (NULL, 'ChickenMonkey', 'C#');

INSERT into exercises
VALUES
    (NULL, 'Planet List', 'Java');

-- CREATE 3 INSTRUCTORS
INSERT into instructors
VALUES
    (NULL, 'Joe', 'Shepherd', '@joes', 'Python', 1);

INSERT into instructors
VALUES
    (NULL, 'Bryan', 'Nilsen', '@bryans', 'C#', 1);

INSERT into instructors
VALUES
    (NULL, 'Madi', 'Pepper', '@madis', 'JavaScript', 1);

UPDATE instructors
SET cohortId = 2
WHERE id = 2;

UPDATE instructors
SET cohortId = 3
WHERE id = 3;

-- CREATE 7 STUDENTS
INSERT into students
VALUES
    (NULL, 'Daniel', 'Meza', '@daniels', 1);

INSERT into students
VALUES
    (NULL, 'John', 'Bain', '@johns', 1);

INSERT into students
VALUES
    (NULL, 'Felipe', 'Moura', '@felipes', 1);

INSERT into students
VALUES
    (NULL, 'Faith', 'Magras', '@faiths', 2);

INSERT into students
VALUES
    (NULL, 'Sammy', 'Barker', '@sammys', 2);

INSERT into students
VALUES
    (NULL, 'Grace', 'Hardin', '@graces', 3);

INSERT into students
VALUES
    (NULL, 'Chris', 'Barker', '@chris', 3);


-- CREATE 2 EXERCISES PER STUDENT

DROP TABLE IF EXISTS studentExercises;

INSERT into studentExercises
VALUES
    (NULL, 1, 1);

INSERT into studentExercises
VALUES
    (NULL, 1, 2);

INSERT into studentExercises
VALUES
    (NULL, 2, 2);

INSERT into studentExercises
VALUES
    (NULL, 2, 3);

INSERT into studentExercises
VALUES
    (NULL, 3, 3);

INSERT into studentExercises
VALUES
    (NULL, 3, 4);

INSERT into studentExercises
VALUES
    (NULL, 4, 4);

INSERT into studentExercises
VALUES
    (NULL, 4, 1);

INSERT into studentExercises
VALUES
    (NULL, 5, 5);

INSERT into studentExercises
VALUES
    (NULL, 5, 1);

INSERT into studentExercises
VALUES
    (NULL, 6, 2);

INSERT into studentExercises
VALUES
    (NULL, 6, 4);

INSERT into studentExercises
VALUES
    (NULL, 7, 3);

INSERT into studentExercises
VALUES
    (NULL, 7, 5);

select s.id,
    s.first,
    s.last,
    s.slack,
    s.cohortId,
    c.name
from students s
    join cohorts c on s.cohortId = c.id
order by s.cohortId;

SELECT *
FROM students;

select i.id,
    i.first,
    i.last,
    i.slack,
    i.cohortId,
    i.specialty,
    c.name
from instructors i
    join cohorts c on i.cohortId = c.cohortId
order by i.cohortId;

select
    e.Id exerciseId,
    e.Name,
    s.id,
    s.first,
    s.last
from exercises e
    join studentExercises se on se.exerciseId = e.Id
    join students s on s.Id = se.studentId;

CREATE TABLE instructorExercises
(
    id INTEGER NOT NULL PRIMARY KEY,
    instructorId INTEGER NOT NULL,
    studentId INTEGER NOT NULL,
    exerciseId INTEGER NOT NULL,
    FOREIGN KEY(studentId) REFERENCES students(id),
    FOREIGN KEY(exerciseId) REFERENCES exercises(id),
    FOREIGN KEY(instructorId) REFERENCES instructors(id)
);

INSERT into instructorExercises
VALUES
    (NULL, 1, 1, 1);

INSERT into instructorExercises
VALUES
    (NULL, 1, 1, 2);

INSERT into instructorExercises
VALUES
    (NULL, 1, 2, 2);

INSERT into instructorExercises
VALUES
    (NULL, 1, 2, 3);

INSERT into instructorExercises
VALUES
    (NULL, 1, 3, 3);

INSERT into instructorExercises
VALUES
    (NULL, 1, 3, 4);

INSERT into instructorExercises
VALUES
    (NULL, 2, 4, 4);

INSERT into instructorExercises
VALUES
    (NULL, 2, 4, 1);

INSERT into instructorExercises
VALUES
    (NULL, 2, 5, 5);

INSERT into instructorExercises
VALUES
    (NULL, 2, 5, 1);

INSERT into instructorExercises
VALUES
    (NULL, 3, 6, 2);

INSERT into instructorExercises
VALUES
    (NULL, 3, 6, 4);

INSERT into instructorExercises
VALUES
    (NULL, 3, 7, 3);

INSERT into instructorExercises
VALUES
    (NULL, 3, 7, 5);

select
    e.Id exerciseId,
    e.Name as 'exercise name',
    s.id,
    s.first as 'student firstname',
    s.last as 'student lastname',
    i.first as 'instructor firstname',
    i.last as 'instructor lastname'
from exercises e
    join instructorExercises ie on ie.exerciseId = e.Id
    join instructors i on ie.instructorId = i.id
    join students s on ie.studentId = s.Id
order by e.name;


