num = int(input("enter the weather in degrees "))
willRain = False

if num < 11:
    clouds = str(input("are there clouds today? (yes/no)"))
    
    if clouds == "yes":
        willRain = True

if willRain == True:
    print("it will rain today")
else:
    print("no rain")

print("bye")

