num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))


total=0
location=1
while num1>0:
    for i in range (num1%10):
        total+=(num2%10)*location
        location*=10
    num1//=10
    num2//=10
# print(total)

counter =0
temp_total=total
while temp_total>0:
    counter+=1
    temp_total//=10
new_total=0
location=1
if counter>9:
    for i in range(9):
        new_total+=(total%10)*location
        location*=10
        total//=10
    print(new_total)
else:
    print(total)
    


