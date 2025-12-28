def star_matrix (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == i:
                matrix[i][i] = " * "
            else:
                matrix[i][j]="   "

    for i in range(len(matrix)):
        matrix[i][-1-i] = " * "

def print_matrix (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end="")
        print()

def main():
    m1 = [[None] * 8 for i in range(8)]
    star_matrix(m1)
    print_matrix(m1)

if __name__=="__main__":
    main()
