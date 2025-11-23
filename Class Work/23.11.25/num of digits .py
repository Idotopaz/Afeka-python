num = int(input("input a number: "))

counter = 0
while num !=0:
    counter +=1
    num //=10
print(f"the number has {counter} digits")
    