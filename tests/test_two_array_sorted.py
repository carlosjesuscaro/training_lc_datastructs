from arrays.two_array_sorted import combine

def test_combine():
    assert combine([1, 2, 3, 4, 5], [6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert combine([1, 3, 5, 7], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 7]