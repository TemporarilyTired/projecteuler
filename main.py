import importlib


def get_module(p):
    try:
        m = importlib.import_module("p"+str(p))
        return m
    except ModuleNotFoundError:
        return False


if __name__ == '__main__':
    problem = None
    while not problem:
        try:
            problem = get_module(int(input()))
        except ValueError:
            print("could not import module, try again: ")

    problem.solve()
