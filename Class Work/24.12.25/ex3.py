def ex3 (list1):
    sum_all=0
    for i in range(len(list1)):
        sum_all+=sum(list1[i])
    return sum_all

print(ex3([[1,2],[3,4,5,8,8],[5,5,6,3,2]]))