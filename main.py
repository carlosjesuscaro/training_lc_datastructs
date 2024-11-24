# This is a sample Python script.
import timeit

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# @profile
def normal_loop(num: int) -> None:
    for i in range(num):
        print(i)

def with_recursion(num: int) -> None:
    if num == 0:
        print(num)
        return
    with_recursion(num - 1)
    print(num)

def recursive_reverse(num: int) -> None:
    print(num)
    if (num - 1) == -1:
        return
    recursive_reverse(num - 1)

# Press the green button in the gutter to run the script.
number = 50
if __name__ == '__main__':
    result = timeit.timeit(f'normal_loop({number})', setup='from __main__ import normal_loop', number=100)
    recursive_time = timeit.timeit(f'with_recursion({number})', setup='from __main__ import with_recursion', number=100)
    reverse_time = timeit.timeit(f'recursive_reverse({number})', setup='from __main__ import recursive_reverse', number=100)
    print(f"Loop execution time: {result:.6f} seconds")
    print(f"Recursion execution time: {recursive_time:.6f} seconds")
    print(f"Reverse execution time: {reverse_time:.6f} seconds")
