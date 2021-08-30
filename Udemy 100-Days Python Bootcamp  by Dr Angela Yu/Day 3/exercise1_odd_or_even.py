def check_number(number):
    if number % 2 == 0:
        print(f"The Given Number {number} is Even")
    else:
        print(f"The Given Number {number} is Odd")

number = int(input("Enter the Number to Check: "))
check_number(number)