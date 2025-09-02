import pytest
from patterns.two_pointers.triplet_sum_to_zero import triplet_sum_to_zero

def test_example_1():
    arr = [-3, 0, 1, 2, -1, 1, -2]
    expected = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    got = triplet_sum_to_zero(arr)
    assert got == expected
    
def test_example_2():
    arr = [-5, 2, -1, -2, 3]
    expected = [[-5, 2, 3], [-2, -1, 3]]
    got = triplet_sum_to_zero(arr)
    assert got == expected
