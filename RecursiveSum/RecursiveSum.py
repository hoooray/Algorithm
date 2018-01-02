def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])

my_list = [1,3,5,7,9]

print sum(my_list)