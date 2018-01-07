def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        small = [i for i in arr[1:] if i <= pivot]
        big = [i for i in arr[1:] if i > pivot]
        return quicksort(small) + [pivot] + quicksort(big)

MYLIST = [1, 3, 55, 7, 9]

print quicksort(MYLIST)
