### 
# Sum of Digits

number = int(input("Enter the Number: "))
sum = 0
while number > 0:
    num = number % 10
    sum += num
    number = number// 10

print(sum)