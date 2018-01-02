def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        return list[0] if list[0] > max(list[1:]) else max(list[1:])

my_list = [1,3,5,7,9]

print max(my_list)