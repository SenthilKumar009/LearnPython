num_list = [12,10,231]

res = []

for num in num_list:
    sum = 0
    for digit in str(num):
        sum += int(digit)
    res.append(sum)

print("Result List : ", res)
