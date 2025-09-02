import pytest
from patterns.two_pointers.remove_duplicates import remove_duplicates, remove_key_duplicates

def test_example_1():
    arr = [2, 3, 3, 3, 6, 9, 9]
    expected = 4
    got = remove_duplicates(arr)
    assert got == expected

def test_example_2():
    arr = [2, 2, 2, 11]
    expected = 2
    got = remove_duplicates(arr)
    assert got == expected

def test_example_3():
    arr = [3, 2, 3, 6, 3, 10, 9, 3]
    key = 3
    expected = 4
    got = remove_key_duplicates(arr, key)
    assert got == expected

def test_example_4():
    arr = [2, 11, 2, 2, 1]
    key = 2
    expected = 2
    got = remove_key_duplicates(arr, key)
    assert got == expected
