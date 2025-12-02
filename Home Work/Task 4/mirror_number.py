num = int(input("input a whole number that is positive: "))

print_num=num
new_num=0
temp=0

while num>0:
    temp=num%10
    new_num=(new_num*10)+temp #0*1+3=3,3*10+2=32,32*10+1=320+1=321
    num//=10

print(print_num,end="")
print(new_num)