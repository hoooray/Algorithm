def bubblesort(arr):
    for i in arr:
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the two item
    return arr


print bubblesort([3, 1, 55, 7, 9])
