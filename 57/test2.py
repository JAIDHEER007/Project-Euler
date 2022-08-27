# Using Recursion to find the Numerator and Denominator in the same function

def recur(n):
    # Base Case
    if n == -2: return (0, 1)
    if n == -1: return (1, 0)

    # Recursive Case
    r1, r2 = recur(n - 1), recur(n - 2)
    aValue = (1 if n == 0 else 2) 
    return (((aValue * r1[0]) + r2[0]), ((aValue * r1[1]) + r2[1])) 

if __name__ == '__main__':
    n = int(input())

    print(*recur(n), sep = " / ")


