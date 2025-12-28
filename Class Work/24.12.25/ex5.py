list1 = [[1,1,1,1],[2,4,4,2],[3,2,1,0]]
the_sum=0
for i in range(len(list1)):
    the_sum+= list1[i][-1-i]
print(the_sum)
