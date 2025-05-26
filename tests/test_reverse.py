from arrays.reverse import reverse

def test_reverse_string():
    assert reverse(['h', 'e', 'l', 'l', 'o']) == ['o', 'l', 'l', 'e', 'h']
    assert reverse(['n', 'a', 'l', 'u']) == [ 'u', 'l', 'a', 'n']