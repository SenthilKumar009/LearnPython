# Write a program in Python to check whether an integer is Armstrong number or not?

def armstrongNumber(number):
    sum = 0
    while(number > 0):
        digit= number %10
        power =digit**2
        sum += (power * digit)
        number //= 10
    
    return sum

number = int(input())

armNumber = armstrongNumber(number)
print(armNumber)

if armNumber == number:
    print('True')
else:
    print('False')

