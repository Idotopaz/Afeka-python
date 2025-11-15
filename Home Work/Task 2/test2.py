num = int(input("Enter a 4 digit number: "))

right_digit = num % 10
#print(right_digit)
middle_right_digit = num//10%10
#print(middle_right_digit)
middle_left_digit = num//100%10
#print(middle_left_digit)
left_digit = num//1000%10
#print(left_digit)

true_if = right_digit-1 == left_digit and middle_right_digit == middle_left_digit

print(true_if)