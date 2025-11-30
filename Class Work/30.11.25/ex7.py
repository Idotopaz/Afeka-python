sign=int(input("how many signs in each line? "))

for i in range(sign+1):
    print(i*"*",end="")
    print((sign-i)*"#")