num1 = int(input("Enter the first number: "))
operator = input("enter the operation: ")
num2 = int(input("Enter the second number: "))

is_input_ok = True

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    result = num1/num2
else:
    is_input_ok = False

if is_input_ok == False:
    print("invalid input")
else:
    print(f"the result is {result}")






