def convert_List_Dict(valueList, keyList):
    n = len(valueList)
    res = []
    for i in range(0, n, 2):
        res.append({keyList[0]: valueList[i], keyList[1]: valueList[i+1]})
    
    return res

valueList = ['SKK', 9, 'SVD', 3, 'SVSD', 17]
keyList = ['Name', 'ID']

print(valueList)
print(keyList)

print(f'Converted Dictionary{convert_List_Dict(valueList, keyList)}')
