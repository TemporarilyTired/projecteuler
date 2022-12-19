def solve():
    from math import factorial
    # 15: find the number of ways you can traverse an n*n grid (n=20) from the top-left to the bottom-right
    # corner by only moving either down or right at each square (the answer is 2n choose n or (2n)! / (n!)^2)
    # runtime: O(n)
    # ans = 137846528820
    n = 20

    ans = factorial(2 * n) // pow(factorial(n), 2)
    print(ans)
