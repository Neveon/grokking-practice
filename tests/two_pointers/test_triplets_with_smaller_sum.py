import pytest
from patterns.two_pointers.triplets_with_smaller_sum import triplets_with_smaller_sum, grokking_triplets_with_smaller_sum

def test_example_1():
    arr = [-1, 0, 2, 3]
    target = 3
    expected = 2
    got = triplets_with_smaller_sum(arr, target)
    assert got == expected
    
def test_example_2():
    arr = [-1, 4, 2, 1, 3]
    target = 5
    expected = 4
    got = triplets_with_smaller_sum(arr, target)
    assert got == expected

def test_example_grokking_1():
    arr = [-1, 0, 2, 3]
    target = 3
    expected = 2
    got = grokking_triplets_with_smaller_sum(arr, target)
    assert got == expected

def test_example_grokking_2():
    arr = [-1, 4, 2, 1, 3]
    target = 5
    expected = 4
    got = grokking_triplets_with_smaller_sum(arr, target)
    assert got == expected
