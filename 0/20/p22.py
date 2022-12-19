def solve():
    # 22: Find the total of all the name scores in the file
    # where a names score is equal to its alphabetical position
    # in the list, multiplied by the sum of the positions of its
    # characters in the alphabet.
    # e.g., COLIN (938th sorted list) => 938 * (3 + 15 + 12 + 9 + 14)
    # runtime: O(n) where n is the number of characters in the list of names
    # ans = 871198282

    def alpha_to_num(c):
        return ord(c) - 64  # ord('A') = 65

    sorted_names = []
    with open("data/p22.txt", "r") as f:
        sorted_names = sorted(f.read().strip('"').split('","'))

    ans = 0
    for i, name in enumerate(sorted_names, start=1):
        ans += i * sum(map(alpha_to_num, name))
    print(ans)
