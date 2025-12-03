num1 = int(input("Input a whole number that is positive: "))
num2 = int(input("Input one digit that is positive: "))

num11=num1
temp = 0
if num1==0:
    counter = 1
else:
    counter = 0
while num1>0:
    temp = num1%10
    if temp == num2:
        counter +=1
    num1//=10

print(f"{num2} appears {counter} times in {num11}")