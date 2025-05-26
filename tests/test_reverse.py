from arrays.reverse import reverse_string

def test_reverse_string():
    assert reverse_string(['h', 'e', 'l', 'l', 'o']) == ['o', 'l', 'l', 'e', 'h']
    assert reverse_string(['n', 'a', 'l', 'u']) == [ 'u', 'l', 'a', 'n']