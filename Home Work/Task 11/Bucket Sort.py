the_list = [2,4,0,3,5,2,5,7,4,0]
print(the_list)

index_count_list = [0]*(max(the_list)+1)
for val in the_list:
    index_count_list[val] += 1

print(index_count_list)

index = 0
for i in range(len(index_count_list)):
    for j in range(index_count_list[i]):
        the_list[index] = i
        index += 1

print(the_list)
txt = "H\te\tl\tl\to"

print(txt)