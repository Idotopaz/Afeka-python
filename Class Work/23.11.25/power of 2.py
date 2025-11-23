num = int(input("How many powers of 2 do you want? "))

power=0
answer=1
while power<num:
    print(f"2 ^ {power} = {answer}")
    answer*=2
    power+=1



