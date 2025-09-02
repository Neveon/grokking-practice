import pytest
from patterns.two_pointers.sort_colors import sort_colors

def test_example_1():
    arr = [1, 0, 2, 1, 0]
    expected = [0, 0, 1, 1, 2]
    got = sort_colors(arr)
    assert got == expected

def test_example_2():
    arr = [2, 2, 0, 1, 2, 0]
    expected = [0, 0, 1, 2, 2, 2]
    got = sort_colors(arr)
    assert got == expected
