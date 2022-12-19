def solve():
    # 1: finds all multiples of integers a and b that are smaller than m.
    # runtime: O(1)
    # ans = 233168
    a = 3
    b = 5
    m = 1000

    # make m an inclusive bound
    m -= 1

    # number of multiples of a, b, and a*b
    na = m // a
    nb = m // b
    nab = m // (a * b)

    # use: sum{1, 2, ..., n-1, n} = n * (n+1) / 2
    natot = na * (na + 1) // 2
    nbtot = nb * (nb + 1) // 2
    nabtot = nab * (nab + 1) // 2

    n = natot * a + nbtot * b - nabtot * a * b
    print(n)
