import pytest
from patterns.two_pointers.squaring_sorted_array import squaring_sorted_array

def test_example_1():
    arr = [-2, -1, 0, 2, 3]
    expected = [0, 1, 4, 4, 9]
    got = squaring_sorted_array(arr)
    assert got == expected

def test_example_2():
    arr = [-3, -1, 0, 1, 2]
    expected = [0, 1, 1, 4, 9]
    got = squaring_sorted_array(arr)
    assert got == expected
