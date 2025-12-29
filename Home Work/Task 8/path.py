def has_path(matrix):
    col = 0
    row=0
    bol=False
    if "-" in matrix[0] or "|" in matrix[0]:
        for i in range(len(matrix)):
            for j in range(-1,-len(matrix[0])-1,-1):
                if matrix[i][j]=="|":
                    col=j
                    row=i+1
                    if row<len(matrix):
                        if matrix[row][col]=="|" or matrix[row][col]=="-":
                            bol=True
                            break
                        else:
                            return False
                    else:
                        bol=True
                        break
                elif matrix[i][j]=="-":
                    col=j-1
                    row=i
                    if col>-len(matrix[0]):
                        if matrix[row][col]=="|" or matrix[row][col]=="-":
                            bol=True
                        else:
                            return False
            else:
                bol=False
        return bol
    else:
        return False

def main():
    matrix = [
        ['a', 'a', 'a', 'a', 'a', 'a'],
        ['a', 'a', 'a', 'a', 'a', '|'],
        ['a', 'a', 'a', '|', '-', '-'],
        ['a', 'a', 'a', '|', 'a', 'a'],
        ['a', 'a', 'a', '|', 'a', 'a']
    ]
    print(has_path(matrix))

if __name__=="__main__":
    main()