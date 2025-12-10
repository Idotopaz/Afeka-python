from collections import Counter

num = int(input("Enter a whole positive number: "))
digit = int(input("Enter one positive digit: "))

godel_modolu = 10 ** digit
multiplier=1


temp1=0
temp2=0
temp3=0
temp4=0

while num>0:
    temp1= num % godel_modolu
    if num>godel_modolu:
        counter=digit
    else:
        temp4=temp1
        counter = 0
        while temp4>0:
            counter+=1
            temp4//=10
    for i in range (counter):
        temp2=temp2*10+(temp1%10)
        temp1//=10

    temp3+=temp2*multiplier
    temp2=0
    multiplier*=godel_modolu
    num//=godel_modolu
print(temp3)