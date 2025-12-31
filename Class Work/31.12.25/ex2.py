def max_tuple (matrix):

    location = []
    max_check = max(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_check :
                max_check = matrix[i][j]
                location = [(i,j)]
            elif matrix[i][j]==max_check:
                location.append((i,j))
    t_max = (max_check)

    print(f"the max is {t_max} and is located at {location}")

max_tuple([[54,5,100,69],
           [14,97,77,72],
           [42,49,100,69],
           [54,21,57,33],
           ])


