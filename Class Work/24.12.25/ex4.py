import random
def random_list (list1):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            list1[i][j]=random.randint(1,99)
    return list1
def print_list (list1):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            print(list1[i][j],end=" ")
        print()
def max_list (list1):
    maximum=0
    maxi = max(list1[0])
    for i in range(1,len(list1)):
        maxi2 = max(list1[i])
        if maxi2 > maxi:
            maximum = maxi2
            maxi = maxi2
        else:
            maximum = maxi
    for i in range(len(list1)):
        if maximum in list1[i]:
            print(f"the max value is: {maximum} which is at [{i},{list1[i].index(maximum)}]")
            break






list2=[[None]*5 for i in range(4)]
random_list(list2)
print_list(list2)
max_list(list2)