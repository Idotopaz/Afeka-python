num = int(input("input a whole number that is positive: "))

counter = 0
temp_num=num
if num<10:
    print(num)
else:
    while temp_num>0:
        counter+=1
        temp_num//=10

    first_dig=0
    if counter%2 !=0:
        i = counter-1
    else:
        i=counter

    dig_position1=10
    dig_position2=1


    total=0
    while i>0: #1234567
        if i%2==0: #i=6 , i=4
            total+=(num%10)*dig_position1 #0+7*10=70,76+5*1000=5076
            dig_position1*=100 #10*100=1000,1000*100=100,000
            num//=10
        else: #i=5 , i=3
            total+=(num%10)*dig_position2 #70+6*1=76,5076+4*100=5467
            dig_position2*=100 #1*100=100 , 100*100=10,000
            num //= 10
        i-=1
    if num>0:
        print(num,end="")
        print(total)
    else:
        print(total)