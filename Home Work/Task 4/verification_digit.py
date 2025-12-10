tz = int(input("enter tz: "))

check_number=tz%10
tz_temp = tz//10
tz//=10

temp1=0
total=0

counter_tz_length=0
multiplier=0

while tz_temp > 0:
    counter_tz_length += 1
    tz_temp //= 10
    
if counter_tz_length == 8:
    multiplier = 2
else:
    multiplier = 1
    
while tz>0:
    temp1=(tz%10)*multiplier
    if temp1>9:
        total += (temp1%10+temp1//10)
        #print(f"+{temp1//10}+{temp1%10}", end="")
    else:
        total+=temp1
        #print(f"+{temp1}", end="")
    if multiplier == 1:
        multiplier = 2
    else:
        multiplier = 1
    tz//=10

# print(total)
expected_check = (10 - (total % 10)) % 10
# print(total-expected_check)
print(expected_check==check_number)





    