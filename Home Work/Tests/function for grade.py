# ...existing code...
def get_valid_grade():
    while True: 
        grade = int(input("what grade did you get? ")) 
        if 0 <= grade <= 100:
            return grade
        print("invalid grade; enter a number between 0 and 100.")

grade = get_valid_grade()
print("ok")
# ...existing code...