def solve():
    # 5: the smallest number that is evenly (=without remainder) divisible by all numbers from 1 to n (= 20)
    # runtime: O()
    # ans = 232792560

    n = 20

    def lcm(a):
        ans = 1
        ps = []
        for x in a:
            for p in ps:
                if not x % p:
                    x //= p
            if x != 1:
                ans *= x
                ps.append(x)
        return ans

    n = lcm(range(1, n + 1))

    return n
