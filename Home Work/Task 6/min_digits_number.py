def new_number_from_min_digits(num1, num2):
    counter1=0
    temp_num1=num1
    temp_num2=num2
    while temp_num1>0:
        counter1+=1
        temp_num1//=10
    counter2=0
    while temp_num2>0:
        counter2+=1
        temp_num2//=10
    if counter1 != counter2:
        return -1
    else:
        total=0
        pose=1
        while num1>0:
            if num1%10<num2%10:
                total+=(num1%10)*pose
            else:
                total +=  (num2 % 10) * pose
            pose *= 10
            num1//=10
            num2//=10
        return total

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print(new_number_from_min_digits(num1,num2))

if __name__=="__main__":
    main()