def solve():
    from math import log, ceil
    # 7: return the nth prime number (n = 10_001)
    # runtime: O((n log n) log log (n log n)), because the length of the sieve is (n log n)
    # and the runtime of Eratosthenes's sieve is (len(sieve) log log len(sieve))
    # ans = 104743
    n = 10_001

    sieve = [False, False] + [True] * (n * ceil(log(n) * 1.2))

    c = 0
    for p, b in enumerate(sieve):
        if b:
            c += 1
            for p2 in range(p * p, len(sieve), p):
                sieve[p2] = False
        if c == n:
            return print(p)
    print("prime", n, ">", len(sieve))