from student import Student
from nss_person import NSSPerson


class Instructor(Student, NSSPerson):
    def __init__(self, first, last, slack, cohort, specialty):
        super().__init__(first, last, slack, cohort)
        self.specialty = specialty

    def set_exercises(self, student, exercises):
        student.exercises.extend(exercises)
