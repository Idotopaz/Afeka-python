has_programing_lesson = input("do you have a programing lesson today? (yes/no): ")
sweets_today = int(input("how many times did you eat sweets today? "))

fun_today = (has_programing_lesson == "yes") or (sweets_today>=2)

print(f"Is it going to be fun today? {fun_today}")