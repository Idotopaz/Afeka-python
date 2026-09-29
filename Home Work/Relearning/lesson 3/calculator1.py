num1 = float(input("enter a number: "))
operator = str(input("enter a mathematical operator (+ - * /): "))
num2 = float(input("enter a second number: "))

if operator == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1*+num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("not a correct operator")
