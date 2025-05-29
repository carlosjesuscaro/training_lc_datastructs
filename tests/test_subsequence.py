from arrays.subsequence import subsequence

def test_subsequence():
    assert subsequence('alianza', 'alianzalima') == True
    assert subsequence('banana', 'anana') == False