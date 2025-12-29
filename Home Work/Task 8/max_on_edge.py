def max_on_edge(numbers):

    maxi0 = max(numbers[0]) #max first list
    maxi_1 = max(numbers[-1]) #max last list
    list1 = [] #new list for left colum
    list2 = [] ##new list for right colum

    for i in range(len(numbers)):
        list1.append(numbers[i][0])
        list2.append(numbers[i][-1])

    maxi_co = max(list1) #max left colum
    maxi_c_1 = max(list2) #max right colum

    max_total = max(maxi0,maxi_co,maxi_c_1,maxi_1) #max all edges

    return max_total

def main():
    numbers = [[8,5,2,77],[44,65,98,54],[100,2,5,33],[6,55,77,54],[1,22,-8,5]]
    print(f"The max is: {max_on_edge(numbers)}")

if __name__ == "__main__":
    main()

