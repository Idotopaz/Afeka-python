num = int(input("input a number: "))

new_num = 0
while num !=0:
    if num%2==0:
        new_num*=10
        new_num+=num%10
        new_num*=10
        new_num+=num%10
        num//=10
    else:
        num//=10

print(new_num)
