# Write a program in Python to check given number is prime or not?

def primeCheck(num):
    if num > 1:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return 'Not Prime'
    
    return 'Prime'


number = int(input())

print(f'The give number {number} is {primeCheck(number)}')