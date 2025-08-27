import pytest
from patterns.sliding_window.fruits_into_baskets import fruits_into_baskets

def test_example_1():
    arr = ['A', 'B', 'C', 'A', 'C']
    expected = 3
    got = fruits_into_baskets(arr)
    assert got == expected

def test_example_2():
    arr = ['A', 'B', 'C', 'B', 'B', 'C']
    expected = 5
    got = fruits_into_baskets(arr)
    assert got == expected

