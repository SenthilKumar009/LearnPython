a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print ('A is Big')
elif a > b and c < b:
    print ('B is Big')
else:
    print('C is Big')