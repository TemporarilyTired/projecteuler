def solve():
    # 24: What is the nth permutation of the digits 0 through 9 when lexographically ordered
    # runtime: O(log n)
    # ans = 2783915460

    # we assume that n < (10!)
    n = 1_000_000

    d_scrambled = 1
    fac = 1
    while n > fac:
        d_scrambled += 1
        fac *= d_scrambled

    d_sorted = 10 - d_scrambled
    ans = "0123456789"[:d_sorted]
    rest = list("0123456789"[d_sorted:])

    # need to switch to 0-indexing for convenience
    n -= 1
    for div in range(d_scrambled, 0, -1):
        fac //= div
        d, n = divmod(n, fac)
        ans += rest.pop(d)
    print(ans)
