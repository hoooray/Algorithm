def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    return arr[0] if arr[0] > max_num(arr[1:]) else max_num(arr[1:])

MYLIST = [1, 3, 5, 7, 9]

print max_num(MYLIST)
