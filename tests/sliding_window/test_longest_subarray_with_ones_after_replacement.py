import pytest
from patterns.sliding_window.longest_subarray_with_ones_after_replacement import longest_subarray_with_ones_after_replacement

def test_example_1():
    arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    expected = 6
    got = longest_subarray_with_ones_after_replacement(arr, k)
    assert got == expected

def test_example_2():
    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    expected = 9
    got = longest_subarray_with_ones_after_replacement(arr, k)
    assert got == expected
