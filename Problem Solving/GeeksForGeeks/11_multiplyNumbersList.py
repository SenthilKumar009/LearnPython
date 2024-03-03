num_list = [1,2,3,4,5,6,7,8,9]

prod = 1

for num in num_list:
    print(f"{str(prod)} * {str(num)} = {prod*num}")
    prod *= num
    
print(prod)