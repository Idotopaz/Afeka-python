A = int(input("input A: "))
B = int(input("input B: "))

if A == 0 and B !=0:
    print("No Solution")    
elif A != 0:
    x = -B/A
    print(f"X value is: {x}")
else:
    print("Infinite solutions")