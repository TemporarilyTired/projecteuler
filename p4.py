def solve():
    # 4: find the largest palindromic number that is a product of two (d=3)-digit numbers
    # runtime: O(10^(2 * d)). xd this is so bad, but there is always a palindrome very early
    # in the search space, so it's doable for d<6.
    d = 6

    # 100 for d = 3, 1000 for d = 4 etc
    minn = d_pow10 = pow(10, d - 1)
    maxn = d_pow10 * 10 - 1

    # unit value of the most significant digit. e.g., 100_000 for maxp = 998_001 (or d = 3)
    d_pow10sq = d_pow10 * d_pow10 // 10

    minp = minn * minn
    maxp = maxn * maxn

    def is_pal(x):
        s = str(x)
        return s[:d] == s[-1:d-1:-1]

    def has_factor_with_d_digits(x):
        return any(not x % p for p in range(minn, maxn+1))

    for n in range(maxp, minp-1, -10):
        if is_pal(np := n + n // d_pow10sq) and has_factor_with_d_digits(np):
            return print(np)

    print(-1)
