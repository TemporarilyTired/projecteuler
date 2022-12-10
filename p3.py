def solve():
    from math import ceil
    # 3: finds the largest prime factor of n = 600851475143
    # runtime: O(sqrt(n))
    n = 600851475143

    while not n & 1:
        if n == 1:
            return print(2)
        n >>= 1
    while not n % 3:
        if n == 3:
            return print(3)
        n //= 3

    for p in range(5, ceil(n ** 0.5), 6):
        while not n % p:
            if n == p:
                return print(p)
            n //= p
        while not n % (p + 2):
            if n == p + 2:
                return print(p + 2)
            n //= p + 2

    print(n)
