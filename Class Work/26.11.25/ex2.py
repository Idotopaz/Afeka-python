num1= int(input("Enter a number: ")) #37
num2= int(input("Enter another number with the same length: ")) #81

temp1 =0
temp2 =0 
dig_location1=10
dig_location2=1
new_num = 0


while num1>0 and num2>0:
    temp1 = (num1%10)*dig_location1 #7,3 - 70 , 3*1000 = 3000
    temp2 = (num2%10)*dig_location2 #1,8 - 1 , 800
    dig_location1 *=100 #1000,10000
    dig_location2 *=100 #100,1000
    new_num += temp1+temp2 #70+1=71 ,+, 3000+800=3800 == 3871

    num1//=10
    num2//=10

print(new_num) #expected output 3871


