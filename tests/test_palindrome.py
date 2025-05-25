from arrays.palindrome import check_palindrome

# Test check_palindrome()
def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False