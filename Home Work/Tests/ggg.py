numbers = [4, 2, 6, 5]
space = max(numbers)

for i in range(max(numbers)):
    for j in range(len(numbers)):
        if numbers[j] >= space:
            print("*", end="")
        else:
            print(" ", end="")

        # רווחים רק אם זה לא האחרון
        if j < len(numbers) - 1:
            print("  ", end="")

    space -= 1
    print()

# קו תחתון
print("_" * (len(numbers) * 3 - 2))

# מספרים
for i in range(len(numbers)):
    print(numbers[i], end="")
    if i < len(numbers) - 1:
        print("  ", end="")