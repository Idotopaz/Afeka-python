tz = int(input("enter tz: "))


bikoret=tz%10
tz_temp = tz//10
tz//=10

temp1=0

while tz>0:

    counter1 = 0
    while tz_temp>0:
        counter1+=1
        tz_temp//=10
    if counter1==7:
        temp1=tz%10


    