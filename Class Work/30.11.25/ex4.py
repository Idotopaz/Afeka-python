num = int(input("enter a number: "))

for i in range (1,num+1):
    if i%7==0:
        print("Boom!",end=" ")
    else:
        print(i,end=" ")



