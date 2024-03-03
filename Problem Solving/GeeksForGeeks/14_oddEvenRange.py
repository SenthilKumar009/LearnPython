start = int(input('Enter the start range:'))
end = int(input('Enter the end range:'))

oddNumList = [num for num in range(start, end+1) if num % 2 != 0]  # List comprehension to filter out odd numbers from
evenNumList = [num for num in range(start, end+1) if num % 2 == 0]  # List comprehension to filter even odd numbers from

print(oddNumList)
print(evenNumList)