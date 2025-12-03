sign=int(input("how many signs in each line? "))
parts = int(input("Enter number of parts: "))

for i in range(sign+1):
    for j in range(parts):
        print(i*"*",end="")
        print((sign-i)*"#",end="")
        print(end="  ")
    print()