import pytest
from patterns.two_pointers.subarrays_with_product_less_than_a_target import subarrays_with_product_less_than_a_target

def test_example_1():
    arr = [2, 5, 3, 10]
    target = 30
    expected = [[2], [2, 5], [5], [5, 3], [3], [10]]
    got = subarrays_with_product_less_than_a_target(arr, target)
    assert got == expected
    
def test_example_2():
    arr = [8, 2, 6, 5]
    target = 50
    expected = [[8], [8, 2], [2], [2, 6], [6], [6, 5], [5]]
    got = subarrays_with_product_less_than_a_target(arr, target)
    assert got == expected

