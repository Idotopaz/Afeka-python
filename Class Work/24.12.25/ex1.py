def ex1 (list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

print(ex1([87,12,56,32],[12,87,12,12,56]))