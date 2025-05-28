from arrays.sorted_square import sorted_square

def test_sorted_square():
    assert sorted_square([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sorted_square([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert sorted_square([-1,-2]) == [1,4]