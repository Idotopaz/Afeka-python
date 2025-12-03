num1=int(input("Enter a number: "))
operator=input("Enter a operator: ")
num2=int(input("Enter a number: "))


while operator == "+":
    print(num1-num2,end="")
    print(num1+num2,end="")
    print(f" = {num1}+{num2}")

    num1 = int(input("Enter a number: "))
    operator = input("Enter a operator: ")
    num2 = int(input("Enter a number: "))
