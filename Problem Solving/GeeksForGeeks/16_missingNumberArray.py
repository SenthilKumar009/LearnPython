def findMissingNumber(numList,n):
    numList.sort()
    
    if n == 2 and numList[0] == 1:
        return 2
    elif n == 2 and numList[0] == 2:
        return 1
    else:
        for i in range(n-1):
            print(f"i={i}")
            if (i < n-1 and (numList[i+1] - numList[i]) != 1):
                print(f"i={i}, {numList[i+1]}, {numList[i]}")
                #return numList[i]+1
        print(f"i={i}, {numList[i]}")
        #return numList[-1] + 1

n = 5
numList = [1,2,3,4]

print(findMissingNumber(numList, n))