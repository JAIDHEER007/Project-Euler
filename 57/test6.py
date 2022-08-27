# Program similar to fibonacci series

def findValues(n):
    res = []

    n1, n2 = 577, 239
    d1, d2 = 408, 169 

    for i in range(8, n + 1):
        n3 = (2 * n1) + n2
        d3 = (2 * d1) + d2

        if len(str(n3)) > len(str(d3)):
            res.append(i)

        n1, n2 = n3, n1
        d1, d2 = d3, d1

    return res

if __name__ == '__main__':
    n = int(input())

    res = findValues(n)

    print(*res, sep = '\n', end = '')