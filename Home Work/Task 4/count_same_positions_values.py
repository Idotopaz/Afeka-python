num1 = int(input("Enter a whole positive number: "))
num2 = int(input("Enter a whole positive number with the same number of digit as the first: "))

temp1=1
temp2=0
counter=0

while num1>0:
    temp1=num1%10
    temp2=num2%10
    if temp1==temp2:
        counter+=1
    num1//=10
    num2//=10

print(f"the numbers aligned {counter} times")


