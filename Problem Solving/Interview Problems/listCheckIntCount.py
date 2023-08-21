lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

intCount = 0

for i in lst:
    if type(i) == int:
        intCount += 1

print(intCount)
