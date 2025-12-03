num = int(input("Input a whole number that is positive: "))

original = num
reversed_num = 0
multiplier = 1

while num > 0: #123
    reversed_num = (reversed_num * 10) + (num % 10) #0*10+3,3*10=30+2,32*=320+1==321
    multiplier *= 10 #10,100,1000
    num //= 10

new_num = original * multiplier + reversed_num #123*1000=123000+321=123321, 100*1000=100001

print(new_num)