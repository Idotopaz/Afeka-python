def create_snake(rows, cols):
    matrix=[[None]*cols for i in range(rows)]
    num=1
    for i in range(-1,-cols-1,-1):
        if i%-2==0:
            for j in range(rows):
                matrix[j][i] = num
                num += 1
        else:
             for j in range(-1, -(rows + 1), -1):
                matrix[j][i] = num
                num += 1

    return matrix



def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(str(i).rjust(2), end=" ")
        print()

def main():
    mat = create_snake(8,5)
    print_matrix(mat)

if __name__=="__main__":
    main()