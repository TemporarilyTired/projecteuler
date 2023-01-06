def solve():
    # 26: Find d < n such that 1/d has the largest recurring cycle in its decimal representation
    # runtime: O()
    # ans = 983
    n = 1000

    hi_ans = (1, 1)

    # proposition 1: The biggest cycles come from prime numbers.
    # proposition 2: The upper limit of the cycle length of 1/d is equal to d-1.
    # Eratosthenes's sieve for primes
    is_prime = [False, False] + [True] * (n - 2)
    s = 0
    for p, b in enumerate(is_prime):
        if b:
            numerator = 10 ** (p * 2 + 1)
            x = str(numerator // p)
            y = str(1 / p)
            c = 1
            cycle = x[0]

            # cycle check not complete (factor in the fact that cycles need not start at the beginning of the decimal
            while x[c:c + len(cycle)] != cycle:
                if c + len(cycle) >= len(x):
                    print("=" * 50, "mmm bad", p, cycle)
                    break
                cycle += x[c]
                c += 1
            if c > hi_ans[0]:
                hi_ans = c, p

            s += p
            for p2 in range(p * p, n, p):
                is_prime[p2] = False

    print(hi_ans[1])
