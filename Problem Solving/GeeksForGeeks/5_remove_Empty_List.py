def removeEmptyList(lst):
    return list(filter(None, lst))

lst = [1,2,3,4,[], [], 7,8,9]

print(lst)
print(removeEmptyList(lst))