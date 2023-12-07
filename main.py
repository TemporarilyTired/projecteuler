import importlib
import sys
from timeit import timeit

# todo: probably switch to returning a string in the solve functions


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
    use_timer = False
    while not problem:
        try:
            inp = input()
            if inp[0] == 't':
                inp = inp[1:]
                use_timer = True
            day_num = int(inp)
            problem = get_module(day_num)
        except ValueError:
            print("Not a valid positive integer, try again: ")

    if use_timer:
        print(timeit(problem.solve, number=10))
    else:
        problem.solve()
