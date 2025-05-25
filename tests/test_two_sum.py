import pytest
from arrays.two_sum import two_sum
from arrays.two_sum import OrderError

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == True
    assert two_sum([2, 7, 11, 15], 1) == False

def test_two_sum_order_error():
    with pytest.raises(OrderError):
        two_sum([1, 2, 4, 3], 3)