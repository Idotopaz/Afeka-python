num=int(input("enter a four digit number"))
firstD=num//1000
secondD=num//100%10
thirdD=num//10%10
fourthD=num%10

print(firstD+secondD==(thirdD+fourthD)*2)