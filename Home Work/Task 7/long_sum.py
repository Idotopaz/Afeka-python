def long_sum(list1, list2):
    total1=0
    total2=0
    pos=0
    for i in range (len(list1)-1,-1,-1):
        total1+=(list1[i])*(10**pos)
        pos+=1
    # print(total1)
    pos=0
    for i in range(len(list2)-1,-1,-1):
        total2 += (list2[i]) * (10 ** pos)
        pos += 1
    # print(total2)
    new_num=total1+total2
    # print(new_num)
    temp = new_num
    counter=0
    while temp>0:
        counter+=1
        temp//=10
    new_list=[None]*counter
    for i in range(len(new_list)-1,-1,-1):
        new_list[i]=new_num%10
        new_num//=10
    return(new_list)

def main():
    list1 = [9, 9, 9, 9]
    list2 = [9, 7]
    print(long_sum(list1,list2))

if __name__=="__main__":
    main()


