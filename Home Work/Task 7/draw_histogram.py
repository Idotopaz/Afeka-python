def draw_histogram(numbers):
    space=max(numbers)
    for i in range (max(numbers)):
        for j in range (len(numbers)):#0
            if numbers[j] >= space :
                print("*",end="  ")
            else:
                print(" ",end="  ")
        space-=1
        print()

    print("_"*(len(numbers)*3))
    for k in range (len(numbers)):
        print(numbers[k],end="  ")

def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    draw_histogram(arr)


if __name__=="__main__":
    main()