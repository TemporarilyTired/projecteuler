def solve():
    # 25: Find i such that the ith fibonacci number is the first fibonacci number with n digits
    # runtime: O(log n) if you assume the fibonacci approximation to be constant time,
    # which it is not because the values can get arbitrarily large. So probably closer to O(n log n) but not sure..
    # ans = 4782
    n = 1000
    pow10n = 10 ** (n - 1)

    # we use rational approximations for sqrt(5) because of floating point size limits
    sqrt5_num, sqrt5_denum = (161, 72) if n < 5000 else (5374978561, 2403763488)
    gr_num = sqrt5_num + sqrt5_denum
    igr_num = sqrt5_denum - sqrt5_num

    def fib_approx_int(x):
        return ((gr_num ** x - igr_num ** x) * sqrt5_denum >> x) // (sqrt5_num * sqrt5_denum ** x)

    # find upper and lower limit
    from math import log10
    # use golden ratio = 1.61803398875 and add a small epsilon and substract a constant margin
    margin = 3
    ans = int(n / log10(1.61805)) - margin

    fib_a = fib_approx_int(ans - 1)
    fib_b = fib_approx_int(ans)
    while fib_b < pow10n:
        fib_a, fib_b, ans = fib_b, fib_a + fib_b, ans + 1
    print(ans)


def solve_v2():
    # 25: Find i such that the ith fibonacci number is the first fibonacci number with n digits
    # runtime: O(log n) if you assume the fibonacci approximation to be constant time,
    # which it is not because the values can get arbitrarily large. So probably closer to O(n log n) but not sure..
    # ans = 4782
    n = 1000
    pow10n = 10 ** (n - 1)

    # we use rational approximations for sqrt(5) because of floating point size limits
    sqrt5_num, sqrt5_denum = (161, 72) if n < 5000 else (5374978561, 2403763488)
    gr_num = sqrt5_num + sqrt5_denum
    igr_num = sqrt5_denum - sqrt5_num

    def fib_approx_exceeds_pown(x):
        return (gr_num ** x - igr_num ** x) * sqrt5_denum >> x > pow10n * (sqrt5_num * sqrt5_denum ** x)

    # find upper and lower limit
    from math import log10, floor, ceil
    # use golden ratio = 1.61803398875 and add a small epsilon and a constant margin
    margin = 4
    lo, hi = floor(n / log10(1.61807)) - margin, ceil(n / log10(1.618025)) + margin

    # note: the upper and lower limit are so close together, it would probably be significantly faster
    # to iterate through the entire (lo, hi) range until we hit the answer
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if fib_approx_exceeds_pown(mid):
            hi = mid
        else:
            lo = mid
    print(hi)