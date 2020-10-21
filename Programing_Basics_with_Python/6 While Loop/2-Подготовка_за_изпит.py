bad_grades = int(input())

count_bd = 0
all_scores = 0
count_scores = 0
number_problems = 0
last_problem = ""


while True:
    name = input()

    if name == "Enough":
        average_scores = all_scores / count_scores
        print(f"Average score: {average_scores:.2f}")
        print(f"Number of problems: {number_problems}")
        print(f"Last problem: {last_problem}")
        break
    number_problems += 1
    last_problem = name
    grade = int(input())
    all_scores += grade
    count_scores += 1
    if grade < 5:
        count_bd += 1
    if count_bd == bad_grades:
        print(f"You need a break, {count_bd} poor grades.")
        break