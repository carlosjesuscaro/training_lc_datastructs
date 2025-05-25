from timeit import timeit


def normal_loop(num: int) -> None:
    for i in range(num):
        # print(i)
        pass

def with_recursion(num: int) -> None:
    if num == 0:
        # print(num)
        pass
        return
    with_recursion(num - 1)
    # print(num)

def recursive_reverse(num: int) -> None:
    # print(num)
    pass
    if (num - 1) == -1:
        return
    recursive_reverse(num - 1)

def recursive_main() -> None:
    number = 500
    result = timeit(f'normal_loop({number})', globals=globals(), number=100)
    recursive_time = timeit(f'with_recursion({number})', globals=globals(), number=100)
    reverse_time = timeit(f'recursive_reverse({number})', globals=globals(), number=100)
    print(f"Loop execution time: {result:.6f} seconds")
    print(f"Recursion execution time: {recursive_time:.6f} seconds")
    print(f"Reverse execution time: {reverse_time:.6f} seconds")
    return None
