import pytest
from patterns.cyclic_sort.find_all_duplicate_numbers import find_all_duplicate_numbers, grokking_find_all_duplicate_numbers

def test_example_1():
    arr = [3, 4, 4, 5, 5]
    expected = [5, 4]
    got = find_all_duplicate_numbers(arr)
    assert got == expected

def test_example_2():
    arr = [5, 4, 7, 2, 3, 5, 3]
    expected = [3, 5]
    got = find_all_duplicate_numbers(arr)
    assert got == expected

def test_example_grok_1():
    arr = [3, 4, 4, 5, 5]
    expected = [5, 4]
    got = grokking_find_all_duplicate_numbers(arr)
    assert got == expected

def test_example_grok_2():
    arr = [5, 4, 7, 2, 3, 5, 3]
    expected = [3, 5]
    got = grokking_find_all_duplicate_numbers(arr)
    assert got == expected

