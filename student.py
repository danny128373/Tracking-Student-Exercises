class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.slack = ""
        self.cohort = ""
        self.exercises = []

    def set_cohort_and_slack(self, cohort):
        self.cohort = cohort
        self.slack = self.cohort + " channel"
