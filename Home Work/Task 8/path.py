def has_path(matrix):
    row = 0
    col = len(matrix[0]) - 1

    while True:
        # Check if we went out of bounds
        if row < 0 or row >= len(matrix) or col < 0:
            return False

        if matrix[row][col] == "|":
            # Found |, check if we reached the last row
            if row == len(matrix) - 1:
                return True  # We made it to the bottom with |
            row += 1  # Move down
        elif matrix[row][col] == "-":
            col -= 1  # Move left
        else:
            # Hit something that isn't | or -, path is broken
            return False

def main():
    matrix = [
        ['a', 'a', 'a', 'a', 'a', '|'],
        ['a', 'a', 'a', 'a', 'a', '|'],
        ['a', 'a', 'a', '|', '-', '-'],
        ['a', 'a', 'a', '|', 'a', 'a'],
        ['a', 'a', 'a', '-', 'a', 'a']
    ]
    print(has_path(matrix))

if __name__=="__main__":
    main()