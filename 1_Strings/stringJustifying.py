print('Hello'.center(20))
print('Hello'.rjust(20))
print('Hello'.ljust(20))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for xlist in tableData:
    for data in xlist:
        print(data, end=' '.rjust(20))
    print()