num1= int(input("Enter a number: ")) #37
num2= int(input("Enter another number with the same length: ")) #81

dig_location=1
new_num = 0


while num1>0 and num2>0:
    new_num += (num2%10)*dig_location
    dig_location *= 10 
    new_num += (num1%10)*dig_location 
    dig_location *= 10

    num1//=10
    num2//=10

print(new_num) #expected output 3871


