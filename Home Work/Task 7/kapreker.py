def is_kaprekar1(num):
    num_squared=num**2 #744 1984
    temp=num_squared
    counter=0
    while temp>0:
        counter+=1
        temp//=10

    for i in range (1,counter+1):
        if(num_squared//(10**i))+(num_squared%(10**i)) == num:
            num1=(num_squared%(10**i))
            num0=(num_squared//(10**i))
            new_list=[num0,num1]
            return new_list
        else:
            new_list=[None]
    return new_list


def is_kaprekar2(num):



def main():
    num=5292
    print(is_kaprekar1(num))

if __name__=="__main__":
    main()