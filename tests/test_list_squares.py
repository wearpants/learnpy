from list_squares import list_squares

def test_empty():
    x = []
    assert len(list_squares(x)) == 0
    assert list_squares(x) is not x

def test_squares():
    x = range(5)
    assert list_squares(x) == [0, 1, 4, 9, 16]
