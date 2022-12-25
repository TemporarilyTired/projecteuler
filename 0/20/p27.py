def solve():
    # 27: Find a * b with -n<a<n and -n<=b<=n such that x^2 + ax + b gives
    # the biggest sequence of only primes for x>=0. (Starting at 0)
    # runtime: O((n / log n)^3)
    # ans = -59231 (n=1000)
    n = 10000

    #              0      1       2     3       ([4]    [5]   [6]    [7]   [8]    [9])
    prime_sieve = [False, False,  True, True] + [False, True, False, True, False, False] * ((n - 4) // 6) \
                + list(bool(x % 3) and (x & 1) for x in range(4 + (n - 4) // 6 * 6, n + 1))

    for p, b in enumerate(prime_sieve):
        if b and p > 4:
            for p2 in range(p * p, n, p):
                prime_sieve[p2] = False

    primes = list(p for p, b in enumerate(prime_sieve) if b)

    def is_prime(x):
        if x < 2:
            return False
        if x <= n:
            return prime_sieve[x]
        if x <= n * n:
            return all(x % p for p in primes)
        if any(not (x % p) for p in primes):
            return False
        for f in range(n // 6 * 6, int(x ** 0.5) + 5, 6):
            if not (x % (f + 1) and x % (f + 5)):
                return False
        return True

    ans_count = 0
    ans_a = 0
    ans_b = 0
    for b in primes:
        for a in primes:
            if a == n:
                break
            c = 1
            while is_prime(c*c + a*c + b):
                c += 1
            if c > ans_count:
                ans_a, ans_b, ans_count = a, b, c

            c = 1
            while is_prime(c * c - a * c + b):
                c += 1
            if c > ans_count:
                ans_a, ans_b, ans_count = -a, b, c
    print(ans_a * ans_b)
