def solve():
    # 18: find the path (moving adjecent as in a symmetric triangle) from top to bottom with the largest sum
    # runtime: O(n^2) where n is the number of layers in the pyramid
    # ans = 1074
    with open("data/p18.txt", "r") as f:
        inp = f.read()
    print(max_triangle_path(inp))


def max_triangle_path(s):
    # parse triangle string
    triangle = [list(map(int, layer.split(" "))) for layer in s.split("\n")]
    h = len(triangle)

    for y in range(h - 2, -1, -1):
        for x in range(y + 1):
            triangle[y][x] += max(triangle[y + 1][x], triangle[y + 1][x + 1])
    return triangle[0][0]
