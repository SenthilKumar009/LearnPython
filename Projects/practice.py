L1 = [10, 20, 30, 25, 32, 45, 50] 
L2 = [80, 70, 78, 55, 62]

print(sum(L1) - sum(L2))

def func(x=1, y=2):
    x = x + y
    y += 1
    print(x,y)

func(y = 2, x = 1)