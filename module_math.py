'''Math helper functions '''

from module_prime import get_prime_factors
from collections import Counter
from itertools import combinations
from functools import reduce
from operator import mul

def get_lcm(numbers):
    ''' Gets the least common multiple (LCM) or
                 least common denominator (LCD) of given numbers
    Args:
        numbers - list of numbers
    Return:
        the LCM of LCD
    '''
    ''' Dictionary of count per prime numbers holds only the max count of each prime number
    the concept of prime factorization'''
    max_count_prime = {}

    ''' Loop thru the numbers and get max count of prime factor for each'''
    for i in numbers:
        factors = []
        get_prime_factors ( i, factors )
        idict = dict(Counter(factors))
        for k,v in idict.items():
            if k in max_count_prime.keys():
                if idict[k] > max_count_prime[k]:
                    max_count_prime[k] = v
            else:
                max_count_prime[k] = v

    product = 1
    for k,v in max_count_prime.items():
        product *= k ** v

    return product

def get_divisors(n, add_1=True, add_n=True):
    '''Gets the divisors of a number
    Args:
        number
    Return:
        list of divisors
    '''
    prime_factors = []
    get_prime_factors ( n, prime_factors )
    divisors = []
    if add_1:
        divisors.append(1)
    if add_n:
        divisors.append(n)

    for i in range(1, len(prime_factors)):
        factors = [ reduce(mul, tupl) for tupl in set ( list ( combinations (prime_factors, i)) )]
        for f in factors:
            divisors.append( n // f)
    return list(set(divisors))

