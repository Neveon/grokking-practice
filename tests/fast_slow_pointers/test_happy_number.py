import pytest
from patterns.fast_slow_pointers.happy_number import find_happy_number

def test_example_1():
    expected = True
    got = find_happy_number(23)
    assert got == expected

def test_example_2():
    expected = False
    got = find_happy_number(12)
    assert got == expected

