def solve():
    # 4: find the largest palindromic number that is a product of two (d=3)-digit numbers
    # runtime: O(10^(2 * d))
    # ans = 906609
    d = 3

    minn = pow(10, d - 1)
    maxn = minn * 10

    def is_pal(x):
        s = str(x)
        return s == s[::-1]

    print(max(filter(is_pal, (x * y for x in range(minn, maxn) for y in range(x, maxn)))))


def solve_deprecated():
    # this method sucks im not gonna keep trying to get this working

    # 4: find the largest palindromic number that is a product of two (d=3)-digit numbers
    # runtime: O(10^(2 * d)). xd this is so bad, but there is always a palindrome very early
    # in the search space, so it's doable for d<7.
    d = 3

    # 100 for d = 3, 1000 for d = 4 etc
    minn = d_pow10 = pow(10, d - 1)
    maxn = d_pow10 * 10 - 1

    # unit value of the most significant digit. e.g., 100_000 for maxp = 998_001 (or d = 3)
    d_pow10sq = d_pow10 * d_pow10 * 10

    minp = minn * minn
    maxp = maxn * maxn

    def is_pal(x):
        s = str(x)
        return s[:d] == s[-1:d-1:-1]

    def has_factor_with_d_digits(x):
        return any(not x % p for p in range(minn, maxn+1))

    for n in range(maxp // 10 * 10, minp-1, -10):
        if is_pal(np := n + n // d_pow10sq) and has_factor_with_d_digits(np):
            return print(np)

    print(-1)
