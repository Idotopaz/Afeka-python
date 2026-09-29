height = float(input("height: "))
weight = float(input("weight: "))
bmi = weight/height**2



if bmi<18.5:
    print(f"your bmi is {bmi} and you are under weight")
elif bmi>=18.5 and bmi<=25:
    print(f"your bmi is {bmi} and you are normal weight")
else:
    print(f"your bmi is {bmi} and you are over weight")