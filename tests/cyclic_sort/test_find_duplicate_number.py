import pytest
from patterns.cyclic_sort.find_duplicate_number import find_duplicate_number

def test_example_1():
    arr = [1, 4, 4, 3, 2]
    expected = 4
    got = find_duplicate_number(arr)
    assert got == expected

def test_example_2():
    arr = [2, 1, 3, 3, 5, 4]
    expected = 3
    got = find_duplicate_number(arr)
    assert got == expected

def test_example_3():
    arr = [2, 4, 1, 4, 4]
    expected = 4
    got = find_duplicate_number(arr)
    assert got == expected
