from itertools import count


def find_col_with_most_appearances(letters, ch):
    col = -1
    counter1=0
    counter2=0
    for i in range(len(letters[0])):
        if counter1<counter2:
            col = i-1
            counter1=counter2
        counter2=0
        for j in range(len(letters)):
            if letters[j][i] == ch:
                counter2+=1


    return col

def main ():
    matrix=[['t','k','a','d'],
            ['a','k','a','f'],
            ['a','f','a','l']]
    char='o'
    h=find_col_with_most_appearances(matrix,char)
    print(f"{char} appers in colum:{h}")

if __name__ == "__main__":
    main()