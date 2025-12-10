import successive_number

def get_dividers_sum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

def are_friends(num1,num2):
    return get_dividers_sum(num1)==num2 and get_dividers_sum(num2)==num1

def main():
    print(are_friends(num1=int(input("1: ")),num2=int(input("2: "))))
    successive_number.create_successive_number

if __name__=="__main__":
    main()
    