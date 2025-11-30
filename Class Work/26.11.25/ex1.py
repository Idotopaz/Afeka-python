num = int(input("Enter a number: ")) #1234

new_num=0
temp1=0 #4
temp2=1 #10,100

while num>0:
    temp1 = num%10 #4,3,2
    if temp1 %2 ==0: #4zogi?2
        temp1 *= temp2 # 4*1=4 ,2*10=20
        temp2 *= 10 #1*10+10
        new_num += temp1 #0+4=4,4+20=24
    num //=10 #1234//10=123,12,1,0
print(new_num)


