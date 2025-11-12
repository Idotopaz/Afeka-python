num1=int(input("enter a 3 digit number: "))

#num1=264 dig0-4 
num1_dig0=num1%10
num1_dig1=num1//10%10
num1_dig2=num1//100%10

num2=int(input("enter a 3 digit number: "))

#num2=462 dig0-2
num2_dig0=num2%10
num2_dig1=num2//10%10       
num2_dig2=num2//100%10

print(num1_dig0==num2_dig2 and num1_dig1==num2_dig2 and num1_dig2==num2_dig0 and (num1*num2)%11 == 0)

#fix at home









