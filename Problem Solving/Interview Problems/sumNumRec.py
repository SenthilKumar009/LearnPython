# Write a program in Python to find sum of digits of a number using recursion?

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

# Test the function.
print(sum_digits(1234))