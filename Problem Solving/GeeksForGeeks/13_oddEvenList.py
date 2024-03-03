num_list = [1,2,3,4,5,6,7,8,9]

oddNumList = [num for num in num_list if num % 2 != 0]  # List comprehension to filter out odd numbers from
evenNumList = [num for num in num_list if num % 2 == 0]  # List comprehension to filter even odd numbers from

# for num in num_list:
#     if num %2 == 0:
#         oddNumList.append(num)
#     else:
#         evenNumList.append(num)
        
print(oddNumList)
print(evenNumList)