def solve():
    # 21: find the sum of all amicable number under n=10000
    # where a is an amicable number if there is an a != b such that
    # the sum of proper divisors of a is equal to b and
    # the sum of proper divisors of b is equal to a.
    # runtime: O(n log n), because the number of array accesses is equal to
    # n/2 + n/3 + n/4 + .. + n/(n/2), which is equal to
    # n multiplied by the sum of first n terms of the harmonic series.
    # ans = 31626

    n = 10_000
    ans = 0
    # inspired by Eratosthenes's sieve
    # array holding the sum of divisors of an index
    sum_divisors = [0, 1] + [1] * (n - 2)
    for d in range(2, (n >> 1)):
        if sum_divisors[d] < d and sum_divisors[sum_divisors[d]] == d:
            ans += d + sum_divisors[d]
        for md in range(d << 1, n, d):
            sum_divisors[md] += d
    for d in range((n >> 1), n):
        if sum_divisors[d] < d and sum_divisors[sum_divisors[d]] == d:
            ans += d + sum_divisors[d]

    print(ans)
