num=int(input("input a 4 digit number "))
first_digit=num//1000
#print(first_digit)
second_digit=num//100%10
#print(second_digit)
third_digit=num//10%10
#print(third_digit)
fourth_digit=num%10
#print(fourth_digit)

print(first_digit==fourth_digit and second_digit==third_digit and num%3 == 0)