def solve():
    # 23: Find all positive numbers which cannot be expressed as the sum of an abundant number
    # An abundant number is a number where the sum of its divisors is bigger that the number itself
    # runtime: O(n log n)
    # ans = 4179871

    # all numbers >28123 can be expressed as the sum of two abundant numbers
    n = 28_123

    abunds = set()
    expressable = set()

    # check if s is abundant. If so, add all sums with other abundants to the expressables
    def check_div_sum(s):
        if sum_divisors[s] > s:
            abunds.add(s)
            nonlocal expressable
            expressable |= set(s + xx for xx in abunds)

    # inspired by Eratosthenes's sieve
    # array holding the sum of divisors of an index
    sum_divisors = [0, 1] + [1] * (n - 2)
    for d in range(2, (n >> 1)):
        check_div_sum(d)
        for md in range(d << 1, n, d):
            sum_divisors[md] += d
    for d in range((n >> 1), n):
        check_div_sum(d)

    ans = 0
    for x in range(n):
        if x not in expressable:
            ans += x
    print(ans)
