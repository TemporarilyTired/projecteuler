def solve():
    # 20: find the sum of the digits of n! (n=100)
    # We could, of course, just calculate n!, because python, but we will not!
    # Although we eventually gave in and just did no optimization at all
    # runtime: O(n^2)
    # ans = 648
    n = 100

    def mult_list(num_list, x):
        res = []
        carry = 0
        for d in num_list:
            carry, cd = divmod(d * x + carry, 10)
            res.append(cd)
        while carry:
            carry, cd = divmod(carry, 10)
            res.append(cd)
        return res

    # (truly) divide the list by 2
    def shiftr_list(num_list):
        res = []
        carry = 0
        for d in num_list:
            cd = (d >> 1) + carry
            carry = 5 * (d & 1)
            res.append(cd)
        return res

    num = [1]
    for m in range(2, n+1):
        while not m % 10:
            m //= 10
        num = mult_list(num, m)

    ans = sum(num)
    print(ans)
