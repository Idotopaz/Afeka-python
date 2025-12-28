def ex2 (list1):
    mini = min(list1)
    return [i for i in range(len(list1)) if mini == list1[i]]


print(ex2([6,14,12,14,12,2,14,6,2,2]))