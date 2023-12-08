import importlib
import math
import sys
from timeit import timeit


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
        single_run_time = timeit(problem.solve, number=1)
        reps = 1.0 / single_run_time
        if reps <= 1:
            print(f"1 rep in {single_run_time:.8g}s")
        else:
            log10_reps = int(math.log10(reps) + 0.5)
            rounded_log10_reps = min(1_000_000, log10_reps)
            reps = 10 ** rounded_log10_reps
            print(f"{reps} rep(s) in {timeit(problem.solve, number=reps):.8g}s")

    print(problem.solve())
