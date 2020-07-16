class Cohort():
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []

    def setInstructors(self, instructors):
        self.instructors.extend(instructors)

    def setStudents(self, students):
        self.students.extend(students)
