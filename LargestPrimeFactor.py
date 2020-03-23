'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def isPrime(n): 

    if n <= 1: 
        return False
  
    for i in range(2, n): 
        if n % i == 0: 
            return False; 
  
    return True
  
factor = 600851475143
largestPrime = 0

for i in range(2,factor):
    if(factor % i == 0 and isPrime(i)):
        largestPrime = i

print(largestPrime)
