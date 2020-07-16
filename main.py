from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

# Exercises
cash_to_coins = Exercise("Cash To Coins", "Python")
nutshell = Exercise("Nutshell", "JavaScript")
english_idioms = Exercise("English Idioms", "Java")
planet_list = Exercise("Planet List", "C#")

# Cohorts
cohort40 = Cohort("Cohort 40")
cohort41 = Cohort("Cohort 41")
cohort42 = Cohort("Cohort 42")

# Students
daniel_meza = Student("Daniel", "Meza")
daniel_meza.set_cohort_and_slack("Cohort 40")
brandy_antonio = Student("Brandy", "Antonio")
brandy_antonio.set_cohort_and_slack("Cohort 41")
harvey_mendoza = Student("Harvey", "Mendoza")
harvey_mendoza.set_cohort_and_slack("Cohort 42")
jesus_vazquez = Student("Jesus", "Vazquez")
jesus_vazquez.set_cohort_and_slack("Cohort 40")

# Instructors
joe_shepherd = Instructor("Joe", "Shepherd", "JavaScript")
bryan_nilsen = Instructor("Bryan", "Nilsen", "C#")
madi_pepper = Instructor("Madi", "Pepper", "Python")

# Assigning students to cohort
cohort40.setStudents([daniel_meza, jesus_vazquez])
cohort41.setStudents([brandy_antonio])
cohort42.setStudents([harvey_mendoza])

# Assigning exercises to each student
joe_shepherd.set_exercises(daniel_meza, [nutshell.name, cash_to_coins.name])
bryan_nilsen.set_exercises(brandy_antonio, [nutshell.name, planet_list.name])
madi_pepper.set_exercises(
    harvey_mendoza, [english_idioms.name, planet_list.name])
joe_shepherd.set_exercises(
    jesus_vazquez, [english_idioms.name, cash_to_coins.name])

# Adding instructors to cohorts
cohort40.setInstructors([joe_shepherd])
cohort41.setInstructors([bryan_nilsen])
cohort42.setInstructors([madi_pepper])

# Print students and their exercises
print(f"{daniel_meza.first} {daniel_meza.last} is working on {' and '.join(daniel_meza.exercises)}.")
print(f"{brandy_antonio.first} {brandy_antonio.last} is working on {' and '.join(brandy_antonio.exercises)}.")
print(f"{harvey_mendoza.first} {harvey_mendoza.last} is working on {' and '.join(harvey_mendoza.exercises)}.")
print(f"{jesus_vazquez.first} {jesus_vazquez.last} is working on {' and '.join(jesus_vazquez.exercises)}.")
