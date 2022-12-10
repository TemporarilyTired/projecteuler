def solve():
    # 2: finds the sum of all even fibonacci numbers that do not exceed m = 4 million
    # runtime: O(g_log m) where g_log is the logarithm the golden ratio as base
    # ans = ...
    m = 4_000_000
    ans = 0
    a, b = 1, 2

    while b <= m:
        ans += b
        a, b = a + 2 * b, 2 * a + 3 * b
    print(ans)
    print(ans)


def solve2():
    from math import log
    # 2: finds the sum of all even fibonacci numbers that do not exceed m = 4 million
    # IDEA: we can take the logarithm of m base golden ratio and that will be the
    # number of fibonacci numbers smaller than m.
    # runtime: probably also O(g_log m) but way worse that the original solution
    GOLDEN_RATIO = (1 + 5**0.5) / 2
    PHI = -1 / GOLDEN_RATIO
    m = 4_000_000

    # every 3rd number in the fibonacci seq. is even
    n_even = int((log(m, GOLDEN_RATIO) + 2) // 3)

    # I did not find a fast way to get the sum of evens from the first n fibonacci numbers
    # making this solution objectively garbage
    ans = 0
    a, b = 1, 2
    for _ in range(n_even):
        ans += b
        a, b = a + 2 * b, 2 * a + 3 * b
    print(ans)
