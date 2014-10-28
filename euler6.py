
'''Problem 6
   Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''

''' square of sum - sum of squares '''
print (sum (x for x in range (101)) ** 2 - sum (x*x for x in range (101)))


