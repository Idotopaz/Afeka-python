pi = 3.14

radius1 = float(input("input a circle radius: "))
radius2 = float(input("input a circle radius: "))

area1= pi*radius1**2
area2= pi*radius2**2

if area1 > area2:
    print("area 1 is bigger")
else:
    print("area 2 is bigger")


