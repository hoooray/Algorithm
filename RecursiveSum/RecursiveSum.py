def sum_num(arr):
    if arr == []:
        return 0
    return arr[0] + sum_num(arr[1:])

MYLIST = [1, 3, 5, 7, 9]

print sum_num(MYLIST)
