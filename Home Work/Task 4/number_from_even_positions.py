num = int(input("input a whole number that is positive: "))

number_position = 1
new_number=0
counter=0

while num>0: 
    if counter%2==0:
        new_number+=(num%10)*number_position
        number_position*=10
    counter+=1
    num//=10

print(new_number)


