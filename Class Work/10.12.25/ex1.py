def draw_isosceles_triangle(base,distance):
    for i in range (1,base+1):
        print(" "*distance,end="")
        print((" *"*i).center(base*2))

base = int(input())
distance = int(input())

draw_isosceles_triangle(base,distance)

