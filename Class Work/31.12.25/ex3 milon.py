def count_divisors (num):
    counter=0
    for i in range(2,num):
        if num%i==0:
            counter+=1
    return counter

def group_numbers_by_divisors (num):

    milon=dict()
    for i in range(num):
        cd=count_divisors(i)
        if cd not in milon.keys():
            milon[cd]=[]
        milon[cd].append(i)
    return milon

def pretty_print_dictionary_with_lists(dic):
    for key in dic:
        print(f"{key}-->{dic[key]}")

def find_location_for_each_value(matrix):
    dic=dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] not in dic.keys():
                dic[matrix[i][j]]=[]
            dic[matrix[i][j]].append((i,j))
    return dic

matrix=[[1,2,3],
        [4,1,6],
        [2,8,1]
        ]

print(find_location_for_each_value(matrix))
pretty_print_dictionary_with_lists(find_location_for_each_value(matrix))