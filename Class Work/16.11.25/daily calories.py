age = float(input("how old? "))
hight = float(input("how tall? in cm: "))

if age<0 or age>8 or hight or hight<40 or hight>140:
    print("invalid input")
    exit()

if age >= 0 and age < 3:
    calories = 700
else:
    if hight >= 40 and hight <= 100:
        calories = 900
    else:
        calories = 1200

print(f"the kid needs to eat {int(calories)} calories")



        
        
