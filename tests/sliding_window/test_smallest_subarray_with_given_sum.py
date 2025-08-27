import pytest
from patterns.sliding_window.smallest_subarray_with_given_sum import smallest_subarray_with_given_sum


def test_example_1():
    arr = [2, 1, 5, 2, 3, 2]
    s = 7 
    expected = 2
    got = smallest_subarray_with_given_sum(arr, s)
    assert got == expected

def test_example_2():
    arr = [2, 1, 5, 2, 8] 
    s = 7
    expected = 1
    got = smallest_subarray_with_given_sum(arr, s)
    assert got == expected

def test_example_3():
    arr = [3, 4, 1, 1, 6]
    s = 8
    expected = 3
    got = smallest_subarray_with_given_sum(arr, s)
    assert got == expected
