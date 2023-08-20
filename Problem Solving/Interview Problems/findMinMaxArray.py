from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
    print(x)

def findMin(arr):
    return min(list(arr))

def findMax(arr):
    return max(list(arr))

print(f'Max value of the given Array: {findMax(array1)}')

print(f'Min value of the given Array: {findMin(array1)}')

arrList = list(array1)
arrList.sort(reverse=True)

print(min(arrList))

print(max(arrList))

def findMinMax(array1):
    min = array1[0]
    max = array1[0]

    for i in range(1, len(array1)):
        if array1[i] < min:
            min = array1[i]
        if array1[i] > max:
            max = array1[i]
    return min, max

arrMin, arrMax = findMinMax(array1)
print("Minimum Value is:", arrMin,"Maximum Value is", arrMax )
        