class OrderError(Exception):
    pass


def check_order(list_input: list) -> bool:
    for i, j in enumerate(list_input):
        if i != len(list_input) - 1:
            if not j <= list_input[i + 1]:
                raise OrderError('List is not in order!')
    return True


def two_sum(sorted_list: list[int], target: int) -> bool:
    """
    Given a sorted list of integers and a target integer, find two numbers such that they add up to target

    Arguments:
    sorted_list {list[int]} -- list of integers
    target {int} -- target integer

    Returns:
    bool -- True if two numbers sum up to target

    Raises:
    ValueError -- raises ValueError if target is not in sorted_list
    TypeError -- raises TypeError if target is not int
    """

    if check_order(sorted_list):
       x, y, condition = 0, len(sorted_list) - 1, False
       while not condition and y > 0 and x < len(sorted_list) - 1:
            tmp_value = sorted_list[x] + sorted_list[y]
            if tmp_value == target:
                return True
            elif tmp_value < target:
                x += 1
            elif tmp_value > target:
                y -= 1
       return condition
    else:
        raise ValueError('Target is not in sorted list!')


def two_sum_main():
    sorted_list = [1, 2, 4, 6, 8, 9, 14, 15]
    target = 13
    tmp = two_sum(sorted_list, target)
    if tmp:
        print('Two numbers from the input list sum the target number')
    else:
        print('No two numbers from the input list sum the target number')
    return None


