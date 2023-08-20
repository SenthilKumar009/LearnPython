a = [10,20,30,20,10,50,60,40,80,50,40]

print(set(a))

print(a)

unq_items = []

for num in a:
    if num not in unq_items:
        unq_items.append(num)

print(unq_items)