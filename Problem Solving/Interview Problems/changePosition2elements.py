numList = [0,1,2,3,4,5,6]

for i in range(0, len(numList), 2):
    #print(numList[i], numList[i+1])
    if i < len(numList)-1:
        numList[i], numList[i+1] = numList[i+1], numList[i]  

print(numList)