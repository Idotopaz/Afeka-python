num1, = int(input())
operator = input()
num2 = int(input())

while operator == "+":
    print(num1 - num2,end="")
    print(num1 + num2)

    num1 = int(input())
    operator = input()
    num2 = int(input())