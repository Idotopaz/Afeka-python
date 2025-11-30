import random

random_number = random.randint(1,100) 
print(random_number)

num = int(input("Try to guess the random number in the least amount of tries: "))
counter =1

while random_number != num:
    if num>random_number:
        print("your number is bigger")
    else:
        print("your number is lower")
    counter +=1
    num = int(input("Try again: "))
print(f"You got the number correct in {counter} tries")
