def solve():
    # 2: finds the sum of all even fibonacci numbers that do not exceed m = 4 million
    # runtime: O(log m), because there are approx. g_log m, fibonacci numbers below m
    # where g_log is the logarithm the golden ratio as base
    # ans = 4613732
    m = 4_000_000

    ans = 2
    a, b = 2, 8

    while b <= m:
        ans += b
        a, b = b, (b << 2) + a
    return ans
