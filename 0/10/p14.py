def solve():
    # 14: find the staring number less than n=1_000_000 that produces the longest collatz chain
    # runtime: O(...)
    # ans = 837799
    n = 1_000_000

    def chain_length(num: int):
        length = 0
        while num.bit_count() > 1:
            length += 1
            if num & 1:
                num = 3 * num + 1
            else:
                num >>= 1
        return length + num.bit_length() - 1

    m = 1
    start = 1
    for i in range(n - 1, 1, -1):
        if chain_length(i) > m:
            start = i
            m = chain_length(i)
    return start
