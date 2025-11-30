print("enter 5 numbers: ")
 
counter=0

for i in range (5):
    num=int(input())
    if num%2 !=0:
        counter+=1
print(f"there are {counter} odd numbers")




