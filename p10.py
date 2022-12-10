def solve():
    # 10: find the sum of all primes below n = 2 million
    # runtime: O(n log log n)
    # ans = 142913828922
    n = 2_000_000

    sieve = [False, False] + [True] * (n - 2)
    s = 0
    for p, b in enumerate(sieve):
        if b:
            s += p
            for p2 in range(p * p, n, p):
                sieve[p2] = False
    print(s)
