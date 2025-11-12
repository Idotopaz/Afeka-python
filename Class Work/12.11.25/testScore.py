
def get_valid_grade():
    while True:
        if 0 <= grade <= 100:
            return grade
        print("invalid grade; enter a number between 0 and 100.")

grade = get_valid_grade()


  
if grade>90:
    print("exellent")
elif grade>80:
    print("very good")
elif grade>=60:
    print("you passed")
    if grade>=60 and grade<=70:
        print("practice more")
elif grade<60:
    print("you failed")












