def solve():
    from math import ceil
    # 12: find x such that the sum of 1-x has over n=500 factors (including 1 and itself)
    # runtime: O(n^3), because we check up to n^2 numbers and for each of those
    # the check if sum up to that point: s ~ n^2, and checking the number of factors
    # takes O(sqrt(s)) = O(n), thus runtime is O(n^2 * n)
    # ans = 76576500
    n = 500

    def n_factors(x):
        ans = 2 - (x & 1)
        for f in range(3, ceil(x ** 0.5 + 0.2)):
            if not x % f:
                ans += 1
        return ans * 2

    s = (n - 2) * (n - 3) // 2
    for i in range(n - 2, n * n):
        s += i
        if n_factors(s) > n:
            return print(s)
