

num = int(input("Enter a number: "))
counter=0
for j in range (num,0,-1):
    print(" "*counter,end="")
    print("* "*j)
    counter+=1
counter=num-1
for j in range (1,num+1):
    print(" "*counter,end="")
    print("* "*j)
    counter-=1

