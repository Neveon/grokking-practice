import pytest
from patterns.sliding_window.max_sum_subarray import find_max_sum_subarray

def test_example_1():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    expected = 9
    got = find_max_sum_subarray(k, arr)
    assert got == expected

def test_example_2():
    arr = [2, 3, 4, 1, 5]
    k = 2
    expected = 7
    got = find_max_sum_subarray(k, arr)
    assert got == expected
