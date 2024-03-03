def count_loop(lst, x):
    sum = 0
    for i in lst:
        if i == x:
            sum += 1
    
    return sum

def count_countMethod(lst, x):
    return lst.count(x)

def count_dict(lst,x):
    occurrence = {item: lst.count(item) for item in lst}
    return occurrence.get(x)


lst = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']

print(count_loop(lst, 'a'))
print(count_countMethod(lst, 'd'))
print(count_dict(lst, 'b'))