sum = 0 
counter = 0 

num=int(input("enter numbers , -1 to stop: "))
while num != -1:
    sum += num
    counter += 1
    num = int(input())

print(f"the avarage of the {counter} numbers is {sum/counter}")
        
        
        