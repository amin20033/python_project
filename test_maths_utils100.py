#  q4. Build a unit test for a simple math function using pytest.

from maths_utils import add

def test_add_positive_numbers():
    assert add(3, 4) == 7

def test_add_negative_numbers():
    assert add(-5, -2) == -7

def test_add_mixed_numbers():
    assert add(10, -3) == 7

def test_add_zero():
    assert add(5, 0) == 5


