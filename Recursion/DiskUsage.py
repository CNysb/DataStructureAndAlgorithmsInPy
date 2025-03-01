import os
import time
from functools import cache


def disk_usage(path: str):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)  # account for direct usage
    if os.path.isdir(path):  # if this is a directory,
        for filename in os.listdir(path):  # then for each child:
            childpath = os.path.join(path, filename)  # compose full path to child
            total += disk_usage(childpath)  # add child’s usage to total
    print(f"{total}\t{path}")  # descriptive output (optional)
    return total  # return the grand total


def time_wrapper(func, *args, **kwargs):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result

    return inner


@cache
def bad_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n <= 1:  # this is the base case
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)  # this is the recursive case


def good_fibonacci(n: int):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return n, 0
    else:
        (a, b) = good_fibonacci(n - 1)
        return a + b, a


if __name__ == "__main__":
    start_time = time.time()
    print(bad_fibonacci(50))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")

    start_time = time.time()
    print(good_fibonacci(50))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
