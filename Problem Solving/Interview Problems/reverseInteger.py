# Write a program to reverse an integer in Python?

def reverse_integer(num):
    # Convert the integer to a string
    num_str = str(num)
    # Reverse the string using slicing
    reversed_str = num_str[::-1]
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    return reversed_num

def reverse_number(num):
    reverse = 0
    while(num > 0):
        digit = num%10
        reverse = reverse * 10 + digit
        num = num // 10
    
    return reverse


number = int(input("Enter the Number: "))

print(f'The reversed Number is: {reverse_integer(number)}')

print(reverse_number(number))