numbers = [1,2,3,4,5,6,7]

print(numbers[::-1])

def reverseArray(numbers):
    reverseArr = []

    for i in range(len(numbers), 0, -1):
        reverseArr.append(i)
    
    return reverseArr


print(reverseArray(numbers))