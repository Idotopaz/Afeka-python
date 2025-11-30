first_number = int(input("input a whole and positive number: ")) #123532
second_number = int(input("input a in the first number: ")) #3

temp1=0
counter=0

while first_number>0: #123532>0
    temp1=first_number%10
    if temp1 == second_number:
        counter+=1
    first_number //= 10
print(counter)