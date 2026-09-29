num2 = int(input("enter a 2 digit number: "))
num1 = int(input("enter a digit (1-9): "))



if num2//10 == num1 or num2%10 == num1:
    print(f"{num1} is in {num2}")
else:
    print(f"{num1} is not in {num2}")