from student import Student


class Instructor(Student):
    def __init__(self, first, last, specialty):
        self.first = first
        self.last = last
        self.slack = ""
        self.cohort = ""
        self.specialty = specialty

    def set_cohort_and_slack(self, cohort):
        self.cohort = cohort
        self.slack = self.cohort + " channel"

    def set_exercises(self, student, exercises):
        student.exercises.extend(exercises)
