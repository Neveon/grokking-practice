import pytest
from patterns.two_pointers.pair_with_target_sum import pair_with_target_sum 

def test_example_1():
    arr = [1, 2, 3, 4, 6]
    target = 6
    expected = [1, 3]
    got = pair_with_target_sum(arr, target)
    assert got == expected

def test_example_2():
    arr = [2, 5, 9, 11]
    target = 11
    expected = [0, 2]
    got = pair_with_target_sum(arr, target)
    assert got == expected
