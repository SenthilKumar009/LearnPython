
### 
# Read input from the user
# Program to swap two number
# Print the numbers

a = int(input("a: "))
b = int(input("b: "))

# Method 0
# c = a
# a = b
# b = c

# Method 1
# a, b = b, a

# Method 2

a = a + b
b = a - b
a = a - b
print("a:" + str(a))
print("b:" + str(b))