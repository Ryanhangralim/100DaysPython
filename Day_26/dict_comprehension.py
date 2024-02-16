import random

names = ["Ryan", "Bob", "Pedro", "Walter", "White", "Junior"]

student_score = {name:random.randint(1, 100) for name in names}
print(student_score)

passed_students = {name:score for (name,score) in student_score.items() if score > 50}
print(passed_students)