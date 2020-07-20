from nss_person import NSSPerson


class Student(NSSPerson):
    def __init__(self, first, last, slack, cohort):
        super().__init__(first, last, slack, cohort)
        self.exercises = []
