name = input()

grade_count = 0
negative_grades = 0
sum_grades = 0

for i in range(1, 12+1):
    if negative_grades == 2:
        print(f"{name} has been excluded at {grade_count-1} grade")
        exit()
    grade = float(input())
    grade_count += 1
    sum_grades = sum_grades + grade
    if grade < 4:
        negative_grades += 1

average_grade = sum_grades / 12
if average_grade >= 4.00:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{name} has been excluded at {grade_count} grade")
