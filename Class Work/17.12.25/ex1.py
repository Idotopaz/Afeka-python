import random
numbers = [None]*10
# sum=0
for i in range (len(numbers)):
    numbers[i] = random.randint(10,100)
    # sum+=numbers[i]
print ("the numbers are: ",numbers)
print ("q1: Even values: ",end="")
for j in range (len(numbers)):
    if numbers[j]%2==0:
        print (numbers[j],end=" ")

print()
print("q2: all 3 divisible: ")
print(numbers)
for j in range (len(numbers)):
    numbers[j]=j*3
print(numbers)

print("q3: increment values in even locations: ")
print("before: ",numbers)
for j in range (0,len(numbers),+2):
    numbers[j]=numbers[j]+1
print("after:  ",numbers)

print("q4: increment values in even locations: ")
print("before: ",numbers)
for j in range (len(numbers)):
    if j%2==0:
        numbers[j]+=1
    if j%3==0:
        numbers[j]-=1
print("after:  ",numbers)

max