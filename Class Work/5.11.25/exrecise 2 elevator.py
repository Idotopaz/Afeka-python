stop=5
between=3

cFloor=int(input("what floor are you on?"))
dest=int(input("what floor are you going to?"))
eFloor=int(input("what floor is the elevator on?"))

sum=(abs(eFloor-cFloor)*between)+(abs(dest-cFloor)*between)+stop

print(f"it will take you {sum} seconds to get to floor {dest}")