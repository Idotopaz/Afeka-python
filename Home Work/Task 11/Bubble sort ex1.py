def reverse_bubble_sort_descending(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] > arr[j - 1]:
                arr[j],arr[j - 1] = arr[j - 1], arr[j]
    return arr

my_list = [12, 5, 3, 19, 8, 1]
sorted_list = reverse_bubble_sort_descending(my_list)
print(f"Sorted List: {sorted_list}")