def solve():
    from math import prod
    # 8: find the sequence of n consecutive digits in the sequence with the highest product
    # runtime: O(len(seq)) where len(seq) is the length of the sequence
    # ans = 23514624000
    with open("data/p8.txt", "r") as f:
        seq = f.read()
    n = 13

    ans = 0
    for ds in seq.split("0"):
        if len(ds) < n:
            continue
        ds = list(map(int, list(ds)))
        pr = prod(ds[:n])
        ans = max(pr, ans)

        for l, r in zip(ds, ds[n:]):
            pr //= l
            pr *= r
            ans = max(pr, ans)

    print(ans)


# A slower implementation that has a runtime complexity that is constant in n (the number of digits in the product)
def solve_v2():
    from queue import Queue
    # 8: find the sequence of n consecutive digits in the sequence with the highest product
    # runtime: O(len(seq)) where len(seq) is the length of the sequence
    # ans = 23514624000
    with open("data/p8.txt", "r") as f:
        n = 13
        cur_prod = 1
        cur_nums = Queue(maxsize=n)
        ans = 0
        while cur_char := f.read(1):
            # parse the next digit
            cur_digit = int(cur_char)

            # if the next digit is a 0 we reset the current product
            if cur_digit == 0:
                cur_nums = Queue(maxsize=n)
                cur_prod = 1
                continue
            if cur_nums.full():
                cur_prod //= cur_nums.get()
            cur_nums.put(cur_digit)
            cur_prod *= cur_digit

            ans = max(cur_prod, ans)

    print(ans)
