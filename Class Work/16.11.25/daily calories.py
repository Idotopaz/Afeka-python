age = float(input("how old? "))

if age<0 or age>8:
    print("invalid input")
    exit()

if age>=0 and age <3:
    calories = 700

elif age>=3 and age <8:
    hight = float(input("how tall? in cm: "))
    if hight<40 or hight>140:
        print("invalid input")
        exit()
    elif hight>=40 and hight<=100:
        calories = 900
    else:
        calories = 1200

print(f"the kid needs to eat {int(calories)} calories")


