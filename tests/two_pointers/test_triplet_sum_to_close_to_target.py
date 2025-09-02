import pytest
from patterns.two_pointers.triplet_sum_to_close_to_target import triplet_sum_to_close_to_target

def test_example_1():
    arr = [-2, 0, 1, 2]
    target = 2
    expected = 1
    got = triplet_sum_to_close_to_target(arr, target)
    assert got == expected
    
def test_example_2():
    arr = [-3, -1, 1, 2]
    target = 1
    expected = 0
    got = triplet_sum_to_close_to_target(arr, target)
    assert got == expected

