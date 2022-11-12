# define the functions needed
# print options to the user
# ask for values
# call the functions
# print the results


def add_numbers(a,b):
   return a + b

def substract_numbers(a,b):
   return a - b

def multiply_numbers(a,b):
   return a * b

def divide_numbers(a,b):
   return a / b

def divide_int_numbers(a,b):
    return a // b

read_action = 1

while read_action == 1:
    a = int(input("Enter the Number 1: "))
    b = int(input("Enter the Number 2: "))

    print("""
              Select the operation to be perform.
              1. Addition
              2. Substraction
              3. Multiplication
              4. Division
              5. Int Division
         """)
    operation = int(input())
    if operation == 1:
        print(f"The sum of the giver numbers: {add_numbers(a, b)}")
    elif operation == 2:
        print(f"The substraction of the given numbers: {substract_numbers(a, b)}")
    elif operation == 3:
        print(f"The multiply of the given numbers: {multiply_numbers(a, b)}")
    elif operation == 4:
        print(f"The division of the given numbers: {divide_numbers(a, b)}")
    elif operation == 5:
        print(f"The integer division of the given numbers: {divide_int_numbers(a, b)}")
    else:
        print("Invalid Input")
        break

    read_action = int(input("Do you want to continue? (0/1): "))