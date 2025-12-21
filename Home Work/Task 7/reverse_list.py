def is_mirror_list (numbers):
    check = False
    temp1=0
    temp2=0
    mirror_right=0
    left=0 #0,0+1=1,1+1=2
    right=len(numbers)-1 #4,4-1=3,3-1=2

    if len(numbers)%2==0:
        rnge = len(numbers)
    else:
        rnge=len(numbers)+1#5+1=6


    for i in range (rnge//2):
        temp1=numbers[right]#321
        pos=0
        # print(temp1)
        while temp1>0:
            pos+=1
            temp1//=10
            # print("hi")

        pos-=1
        temp2=numbers[right]#50
        while temp2>0:
            mirror_right+=(temp2%10)*(10**pos) #1*10^2=100,100+2*10^1=120,120+3*10^0=123/50->5
            pos-=1
            temp2//=10
            # print("hi2")

        # print(numbers[left],"==",end="")
        # print(mirror_right)
        check = numbers[left]==mirror_right
        mirror_right=0
        left+=1
        right-=1

        if check == False:
            return False
            exit()

    if check == True:
        return True



def main ():
    arr=[1,20]
    print(is_mirror_list(arr))

if __name__=="__main__":
    main()










