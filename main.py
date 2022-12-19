import importlib
import sys


def get_dir(p):
    return f"{p // 100 * 100 % 1000}/{p // 10 * 10 % 100}"

def get_module(p):
    try:
        sys.path.append(get_dir(p))
        m = importlib.import_module("p" + str(p))
        return m
    except ModuleNotFoundError:
        if sys.path[-1] == get_dir(p):
            sys.path.pop()
        print("Could not find module:", f"{get_dir(p)}/p{p}")
        return None


if __name__ == '__main__':
    problem = None
    while not problem:
        try:
            problem = get_module(int(input()))
        except ValueError:
            print("Not a valid positive integer, try again: ")

    problem.solve()
