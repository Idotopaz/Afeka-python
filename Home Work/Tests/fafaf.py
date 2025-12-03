
temp1=789
temp2=0
multiplier=1
for i in range(3):
    temp2 = temp2 * multiplier + (temp1 % 10) #0*1+9=9,9*10=90+8=98,98*100=9800+1=9801
    print(temp2)
    temp1 //= 10
    multiplier *=10


test="hi"
print(test.center(8))