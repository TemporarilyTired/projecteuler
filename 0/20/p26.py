def solve():
    # 26: Find d < n such that 1/d has the largest recurring cycle in its decimal representation
    # runtime: O()
    # ans = ..
    n = 1000

    # Eratosthenes's sieve
    is_prime = [False, False] + [True] * (n - 2)
    s = 0
    for p, b in enumerate(is_prime):
        if b:
            s += p
            for p2 in range(p * p, n, p):
                is_prime[p2] = False

    max_comp = 1
    max_prime = 1
    for d in range(1, n):
        x = str(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000//d)
        y = str(1/d)
        c = 1
        cycle = x[0]

        # cycle check not complete (factor in the fact that cycles need not start at the beginning of the decimal
        while c + len(cycle) < len(x) and x[c:c + len(cycle)] != cycle:
            cycle += x[c]
            c += 1
        if is_prime[d]:
            max_prime = max(c, max_prime)
        else:
            max_comp = max(c, max_comp)
        print(d, max_prime, max_comp, is_prime[d], c, x,  y)
