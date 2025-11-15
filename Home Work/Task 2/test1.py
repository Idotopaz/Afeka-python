num = int(input("Enter a 3 digit number: "))

right_digit = num % 10
#print(right_digit)
middle_digit = num//10%10
#print(middle_digit)
left_digit = num//100%10
#print(left_digit)

right_equal_2left = right_digit == 2*(middle_digit+left_digit)

print(right_equal_2left)

