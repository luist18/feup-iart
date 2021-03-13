import time


def measure_search(function, prettyprint_function=None, *args):
    start = time.time()
    result = function(*args)
    end = time.time()

    if prettyprint_function != None:
        prettyprint_function(*result)

    elapsed = end - start

    print()

    print(function.__name__, f"took {elapsed} seconds to run")

    print()
