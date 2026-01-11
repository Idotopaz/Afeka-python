def switch_values(the_list, index_begin, index_end):
    if index_end <= index_begin:
        return the_list
    temp=the_list[index_begin]
    the_list[index_begin]=the_list[index_end]
    the_list[index_end]=temp
    return switch_values(the_list,index_begin+1,index_end-1)

def main():
    print(switch_values([10,20,30,40,50,60],0,5))

if __name__=="__main__":
    main()
