'''Problem 7
   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
   What is the 10 001st prime number?
'''
from module_prime import is_prime

primes = []
n = 2
while len(primes) < 10002:
    if is_prime(n):
        primes.append(n)
    n += 1

print (primes[10000])

