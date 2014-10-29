''' Problem 10 Summation of primes 
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
'''

from module_prime import is_prime

print ( sum ( [ n for n in range(2, 2000000) if is_prime(n) ]) )


