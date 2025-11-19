num = int(input("input a number: "))

sum = 0
while num != 0:
    sum+=num%10
    num //= 10

print(f"the sum is {sum}")



