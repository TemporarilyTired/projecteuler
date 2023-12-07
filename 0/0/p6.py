def solve():
    # 6: return the difference between (1^2 + 2^2 + ... + (n-1)^2 + n^2) and (1 + 2 + ... + n-1 + n)^2
    # return the difference between the sum of squares and the square of the sum of the first (n=100) natural numbers
    # runtime: O(n)
    # ans = 25164150

    n = 100

    def sq(x): return x * x

    sum_of_sqs = sum(map(sq, range(n+1)))

    # use: sum{1, 2, ..., n-1, n} = n * (n+1) / 2
    sq_of_sums = sq(n * (n+1) >> 1)

    print(sq_of_sums - sum_of_sqs)
