# Using Recursion to find the Numerator and Denominator in the same function
# Using Named tuple for better understanding

from collections import namedtuple

frac = namedtuple(typename = 'Fraction', field_names = ['numerator', 'denominator'])

def recur(n):
    # Base Case
    if n == -2: return frac(0, 1)
    if n == -1: return frac(1, 0)

    # Recursive Case
    r1, r2 = recur(n - 1), recur(n - 2)
    aValue = (1 if n == 0 else 2) 
    return frac(((aValue * r1.numerator) + r2.numerator), ((aValue * r1.denominator) + r2.denominator)) 

if __name__ == '__main__':
    n = int(input())

    print(*recur(n), sep = " / ")


