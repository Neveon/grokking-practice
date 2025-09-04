import pytest
from patterns.cyclic_sort.cyclic_sort import cyclic_sort

def test_example_1():
    arr = [3, 1, 5, 4, 2]
    expected = [1, 2, 3, 4, 5]
    got = cyclic_sort(arr)
    assert got == expected

def test_example_2():
    arr = [2, 6, 4, 3, 1, 5]
    expected = [1, 2, 3, 4, 5, 6]
    got = cyclic_sort(arr)
    assert got == expected

def test_example_3():
    arr = [1, 5, 6, 4, 3, 2]
    expected = [1, 2, 3, 4, 5, 6]
    got = cyclic_sort(arr)
    assert got == expected
