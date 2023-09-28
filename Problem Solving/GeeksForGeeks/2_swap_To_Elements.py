def swap_elements(lst, pos1, pos2):
    if pos1 > len(lst) or pos2 > len(lst):
        print("Invalid index")
    else:
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    
    return lst

lst = [1,2,3,4,5,6,7,8,9,0]

pos1 = int(input('Enter the position to swap: '))
pos2 = int(input('Enter the position to swap: '))

print(swap_elements(lst, pos1, pos2))