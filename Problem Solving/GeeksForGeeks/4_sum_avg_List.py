def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def avg_list(lst):
    return float(sum_list(lst))/len(lst)


lst = [1,2,3,4,5,6,7,8,9,10]

print(f'Sum of the List is {sum_list(lst)}')
print(f'Average of the List is {avg_list(lst)}')
