
numList = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

result = []

for i in range(0, len(numList) - 1):
    if (numList[i] == numList[i+1]) and (numList[i] not in result):
        result.append(numList[i])
    else:
        result.append(numList[i+1])

print(result)
