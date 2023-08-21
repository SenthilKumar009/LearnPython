numList = [4, 5, 8, 9, 6, 10]


resultList = []

for i in range(0, len(numList) -1):
    resultList.append(numList[i+1] - numList[i])

print(resultList)