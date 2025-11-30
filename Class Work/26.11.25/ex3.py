num = int(input("enter a number: "))

temp1=0
big_dig=0

while num>0:
    temp1= num%10
    if temp1>big_dig:
        big_dig=temp1

    num//=10

print(big_dig)


