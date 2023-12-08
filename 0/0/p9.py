def solve():
    # 9: given (n=1000) such that a^2 + b^2 = c^2 and a + b + c = n has exactly one solution, find the product of a<b<c
    # runtime: O(n^2)
    # ans = 31875000
    n = 1000

    for a in range(1, n - 2):
        a2 = a * a
        for b in range(a + 1, n - a):
            c2 = (n - a - b) * (n - a - b)
            if a2 + b * b == c2:
                return a * b * (n - a - b)

    return f"no solution for n={n}"
