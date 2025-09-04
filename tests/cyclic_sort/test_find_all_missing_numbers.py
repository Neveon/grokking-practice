import pytest
from patterns.cyclic_sort.find_all_missing_numbers import find_all_missing_numbers

def test_example_1():
    arr = [2, 3, 1, 8, 2, 3, 5, 1]
    expected = [4, 6, 7]
    got = find_all_missing_numbers(arr)
    assert got == expected

def test_example_2():
    arr = [2, 4, 1, 2]
    expected = [3]
    got = find_all_missing_numbers(arr)
    assert got == expected

def test_example_3():
    arr = [2, 3, 2, 1]
    expected = [4]
    got = find_all_missing_numbers(arr)
    assert got == expected

