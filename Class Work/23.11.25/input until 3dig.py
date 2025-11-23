
num = int(input("enter a number: "))
 
while True:               # runs until num has X digits and asks again if not
    counter = 0
    while num!=0:         #counts the digits of a number
        counter+=1
        num//=10
    if counter != 3:      # checks if number has X digits (works for any number written in if)
        num = int(input("enter another number: "))
    else:
        break             # exits the first while loop when num has X digits
    
print (counter)

