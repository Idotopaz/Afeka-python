num = int(input("Enter a number: "))

new_num=0
temp1=0
temp2=1

while num>0:
    temp1 = num%10
    if temp1 %2 ==0:
        temp1 *= temp2
        temp2 *= 10
        new_num += temp1
    num //=10
print(new_num)


