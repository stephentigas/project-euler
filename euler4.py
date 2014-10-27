''' The answer can be placed in nested list comprehensions '''
max ([ x*y for x in range(100, 1000) for y in range (100, 1000) if ( str(x*y) == str(x*y)[::-1] ) ])
