num = int(input("enter the weather in degrees "))
clouds = str(input("are there clouds today? (yes/no)"))

if num < 11 and clouds == "yes":
    print("it is going to rain today")
else:
    print("no rain today")

print("bye")

