# Using Recursion to find the Numerator and Denominator

def recurNumerator(n):
    # Base Case
    if n == -2: return 0
    if n == -1: return 1

    # Recursive Case
    return ((1 if n == 0 else 2) * recurNumerator(n - 1)) + recurNumerator(n - 2) 

def recurDenominator(n):
    # Base Case
    if n == -2: return 1
    if n == -1: return 0

    # Recursive Case
    return ((1 if n == 0 else 2) * recurDenominator(n - 1)) + recurDenominator(n - 2)

if __name__ == '__main__':
    n = int(input())

    print(recurNumerator(n), recurDenominator(n), sep = " / ")


