def count(list):
    if len(list) == 1:
        return 1
    else:
        return 1 + count(list[1:])

my_list = [1,3,5,7,9]

print count(my_list)