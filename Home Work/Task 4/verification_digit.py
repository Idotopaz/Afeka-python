tz = int(input("enter tz: "))

bikoret=tz%10
tz_temp = tz//10
tz//=10

temp1=0
sum=0
round_up=0
counter1 = 0
counter2=0

while tz_temp > 0:
    counter1 += 1
    tz_temp //= 10
if counter1 == 8:
    counter2 = 2
    print(f"here {counter1} , {tz}")
else:
    print(f"here {counter1} , {tz}")
    counter2 = 1
while tz>0:
    if counter2==2:
        temp1=(tz%10)*counter2
        print(f"{temp1}+",end=" ")
        counter2//=2
        if temp1>9:
            sum += (temp1%10+temp1//10)
        else:
            sum+=temp1
    elif counter2==1:
        temp1=(tz%10)*counter2
        counter2*=2
        print(f"{temp1}+",end=" ")
        sum+=temp1
    tz//=10
print(f"={sum}")
round_up = ((sum//10)*10)+10
bdika=(round_up-sum)==bikoret
print(bdika)





    