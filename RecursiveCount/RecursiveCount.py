def count(arr):
    if len(arr) == 1:
        return 1
    return 1 + count(arr[1:])

MYLIST = [1, 3, 5, 7, 9]

print count(MYLIST)
