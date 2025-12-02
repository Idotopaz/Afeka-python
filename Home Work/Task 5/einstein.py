

# print(17//10,"/",85%10)
count=0
for j in range(11,100):
    for i in range (11,100):
            if j%10!=0:
                if (i//10)/(j%10)==i/j and i/j<1:
                    print(f"{(i//10)}/{(j%10)} == {i}/{j}")
                    count+=1
print(count)

