def solve():
    # 16: find the sum of digits of the value of 2^n (n=1000)
    # runtime: O(n) i guess, but bad
    # ans = 1366
    n = 1000
    n2 = 1 << n
    ans = 0

    while n2:
        n2, d = divmod(n2, 10)
        ans += d

    print(ans)
