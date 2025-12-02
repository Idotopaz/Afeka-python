
for i in range(11,100):
    for j in range (11,100):
        if (i//10)/(j//10) == i/j and i/j<1:
            print(f"{(i//10)}/{(j//10)} == {i}/{j}")


