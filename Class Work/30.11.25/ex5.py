num=int(input("enter a 2 digit number: "))

for i in range(1,num+1):
    if (i%10)+(i//10)==5:
        print(i,end=" ")


