import pytest
from patterns.cyclic_sort.find_missing_number import find_missing_number

def test_example_1():
    arr = [4, 0, 3, 1]
    expected = 2
    got = find_missing_number(arr)
    assert got == expected

def test_example_2():
    arr = [8, 3, 5, 2, 4, 6, 0, 1]
    expected = 7
    got = find_missing_number(arr)
    assert got == expected

