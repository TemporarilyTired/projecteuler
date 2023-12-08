def solve():
    from math import prod
    import numpy
    # 11: given the grid, find the n integers in a cardinal or diagonal line in the grid with the highest product
    # runtime: O(n^2)
    # ans = 70600674
    n = 4
    def nonzero_int(x): return int(x) if int(x) else -1  # this will make the solution incorrect for certain inputs
    with open("data/p11.txt", 'r') as raw_grid:
        grid = numpy.array(list(map(lambda x: list(map(nonzero_int, x.strip().split(" "))), raw_grid.readlines())))

    ans = 0

    def iterate_line(line):
        nonlocal ans
        pr = prod(line[:n])
        zeroes = numpy.count_nonzero(line[:n] == -1)
        if not zeroes:
            ans = max(ans, pr)
        for l, r in zip(line, line[n:]):
            zeroes += int(r == -1) - int(l == -1)
            pr //= l
            pr *= r
            if not zeroes:
                ans = max(pr, ans)

    # I do not really know a way to iterate through all directions in a clean way
    # horizontal
    for row in grid:
        iterate_line(row)

    # vertical
    for col in grid.T:
        iterate_line(col)

    # diagonals
    for i in range(1-len(grid), len(grid)):
        iterate_line(numpy.diagonal(grid, i))
        iterate_line(numpy.diagonal(numpy.fliplr(grid), i))

    return ans
