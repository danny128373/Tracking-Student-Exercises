import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = r"\\wsl$\Ubuntu-18.04\home\dm3f90\workspace\python\StudentExercises\studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select s.Id,
                s.first,
                s.last,
                s.slack,
                s.cohortId,
                c.name
            from students s
            join cohorts c on s.cohortId = c.cohortId
            order by s.cohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_cohorts(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Cohort(row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select c.cohortId, c.name
            from cohorts c
            order by c.cohortId
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select ex.id, ex.name, ex.language
            from exercises ex
            order by ex.id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def all_javascript_exercises(self):
        """Retrieve all exercises required to be done in javascript"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select ex.id, ex.name, ex.language
            from exercises ex
            where language = 'JavaScript'
            order by ex.id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def all_python_exercises(self):
        """Retrieve all exercises required to be done in python"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select ex.id, ex.name, ex.language
            from exercises ex
            where language = 'Python'
            order by ex.id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def all_csharp_exercises(self):
        """Retrieve all exercises required to be done in C#"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select ex.id, ex.name, ex.language
            from exercises ex
            where language = 'C#'
            order by ex.id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def all_instructors(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[6], row[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
           select i.id,
                i.first,
                i.last,
                i.slack,
                i.cohortId,
                i.specialty,
                c.name
            from instructors i
            join cohorts c on i.cohortId = c.cohortId
            order by i.cohortId
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)

    def assignments_by_exercise_and_student(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id exerciseId,
                    e.Name,
                    s.id,
                    s.first,
                    s.last
                from exercises e
                join studentExercises se on se.exerciseId = e.Id
                join students s on s.Id = se.studentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

    def student_workload(self):
        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id exerciseId,
                    e.Name,
                    s.id,
                    s.first,
                    s.last
                from exercises e
                join studentExercises se on se.exerciseId = e.Id
                join students s on s.Id = se.studentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(student_name)
                for exercise in exercises:
                    print(f'\t* {exercise}')

    def exercises_assignments_with_students(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
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
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                instructor_name = f'{row[5]} {row[6]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [
                        (student_name, instructor_name)]
                else:
                    exercises[exercise_name].append(
                        (student_name, instructor_name))

            for exercise in exercises.items():
                print(exercise[0])
                for student, instructor in exercise[1]:
                    print(
                        f'\t* Assigned by: {instructor} to {student}.')


reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript_exercises()
reports.all_python_exercises()
reports.all_csharp_exercises()
reports.all_instructors()
reports.assignments_by_exercise_and_student()
print("********************")
print("* Student Workload *")
print("********************")
reports.student_workload()
print("************************")
print("* Exercise Assignments *")
print("************************")
reports.exercises_assignments_with_students()
