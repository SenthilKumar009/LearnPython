n1 = 0
n2 = 1

number = int(input())


for i in range(0, number):
    if i <= 1:
        result = i
    else:
        result = n1 + n2
        n1 = n2
        n2 = result
        #n1, n2 = n2 , n1 + n2
    print(result)
    if number-1 == i:
        print(f'{number}th/rd Sequence in Fibonacci is {result}')