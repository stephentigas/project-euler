'''Module involving prime numbers'''

def is_prime(n):
    '''Checks if the number passed is a prime number
    Args:
      n - the number 
    Return:
      True - if the number is a prime number
      False - if the number is not a prime number
    '''
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def get_prime_factors(n, prime_factors):
  '''Gets the prime factors of a number n and populates to list prime_factors
  Args:
      n - the number 
      prime_factors - list of prime factors
  Return:
      no return, prime factors is populated in the prime_factors list which is a mutable object
  '''
  if is_prime(n):
    prime_factors.append(n)
    return

  if n % 2 == 0:
    prime_factors.append(2)
    get_prime_factors( n // 2, prime_factors )
    return

  if n % 3 == 0:
    prime_factors.append(3)
    get_prime_factors( n // 3, prime_factors )
    return

  for i in range(5, int(n ** 0.5) + 1, 6):
    if n % i == 0:
      prime_factors.append(i)
      get_prime_factors( n // i, prime_factors )
      break
      return

    if n % (i + 2) == 0:
      prime_factors.append(i+2)
      get_prime_factors( n // (i+2), prime_factors )
      break
      return

