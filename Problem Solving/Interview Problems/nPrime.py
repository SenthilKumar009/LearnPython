# Python program to print first n prime numbers?

#function to check if a given number is prime
def isPrime(n):
    if n==1 or n==0:
         return False
    
    for i in range(2,n):
         if(n%i==0):
             return False
    return True



N = 100

for i in range(1,N+1):
    if(isPrime(i)):
        print(i,end=" ")
