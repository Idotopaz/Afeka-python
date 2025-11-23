
test_grade = int(input("Enter your test grade (out of 100): "))
homework_average = int(input("Enter you homework grade average (out of 100): "))
deliverd_task = int(input("Enter how many assignments have you handed in (out of 9): "))

final_grade = 0

if deliverd_task<=4:
    final_grade = 0
elif deliverd_task == 5 or deliverd_task == 6:
    if test_grade>=55:
        final_grade = homework_average*0.2 + test_grade*0.8
    else:
        final_grade = test_grade
elif deliverd_task == 7 or deliverd_task == 8:
    if test_grade<=54:
        if homework_average>=80:
            final_grade = homework_average*0.25 + test_grade*0.75
        else:
            final_grade = homework_average*0.2 + test_grade*0.8
            if test_grade > final_grade:
                final_grade = test_grade
    elif 55<=test_grade:
        if test_grade<homework_average:
            final_grade = homework_average * 0.3 + test_grade*0.7
    else:
        final_grade = test_grade

print(final_grade)