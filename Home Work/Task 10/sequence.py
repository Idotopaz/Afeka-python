def has_sequence(the_list, num):
    if num==0:
        return True

    if num not in the_list or len(the_list)<num:
        return False

    elif the_list[0] != 1:
        the_list.remove(the_list[0])
        return has_sequence(the_list,num)

    elif the_list[num-1]==num:
        return has_sequence(the_list, num-1)
    else:
        the_list.remove(the_list[0])
        return has_sequence(the_list, num)


def main():
    print(has_sequence([3,1,2,3,5,6,3],4))


if __name__=="__main__":
    main()
