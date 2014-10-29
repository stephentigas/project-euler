'''Problem 9 Special Pythagorean triplet'''

print ( [(a,b,c) for a in range(1, 1001) 
                 for b in range (a+1,1001-a) 
                 for c in range (b+1,1001-(a+b)) if (a + b + c == 1000) and ((a*a + b*b) == c*c)] )

