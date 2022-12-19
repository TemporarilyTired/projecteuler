def solve():
    from main import get_module
    m = get_module(18)
    # 67: find the path (moving adjecent as in a symmetric triangle) from top to bottom with the largest sum
    # runtime: O(n^2) where n is the number of layers in the pyramid
    # ans = 7273
    with open("data/p67.txt", "r") as f:
        inp = f.read()
    print(m.max_triangle_path(inp))
