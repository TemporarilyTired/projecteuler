def solve():
    # 13: find the first 10 digits of the sum of the given one-hundred 50-digit numbers
    # runtime: O(IDK, I don't like this problem)
    # ans = 5537376230

    with open("data/p13.txt", 'r') as nums:
        return str(sum(map(lambda x: int(x.strip()), nums.readlines())))[:10]
