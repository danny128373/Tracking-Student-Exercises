from nss_person import NSSPerson


class Student(NSSPerson):
    def __init__(self, first, last, slack, cohort):
        super().__init__(first, last, slack, cohort)
        self.exercises = []

    def __repr__(self):
        return f'{self.first} {self.last} is in {self.cohort}'
