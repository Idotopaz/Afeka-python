num = int(input("Enter a number between 5-10: "))

while num<5 or num>10:
    num = int(input("Invalid value,try again: "))

print("||".rjust(3),end="")
for i in range (1,num+1):
    print(f"{i}".rjust(3),end="|")
print()

for i in range(num+1):
    print("-"*4,end="")
print()

for row in range(1,num+1):   
    print(f"{row}".rjust(2),end="||")

    for col in range (1,num+1):
        print(f"{col*row}".rjust(3),end="|")
    print()
