def create_successive_number(num):
    total=0
    pose=1
    
    while num>0:
        if (num%10)==9:
            total+= 0 * pose
            pose*=10
        else:
            total+=((num%10)+1)*pose
            pose*=10
        num//=10
    return total

def main ():
    num = int(input("Enter a number: "))
    print(create_successive_number(num))

if __name__=="__main__":
    main()