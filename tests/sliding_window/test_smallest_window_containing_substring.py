import pytest
from patterns.sliding_window.smallest_window_containing_substring import smallest_window_containing_substring

def test_example_1():
    string = "aabdec"
    pattern ="abc"
    expected = "abdec"
    got = smallest_window_containing_substring(string, pattern)
    assert got == expected

def test_example_2():
    string = "abdabca"
    pattern = "abc"
    expected = "abc"
    got = smallest_window_containing_substring(string, pattern)
    assert got == expected

def test_example_3():
    string = "adcad"
    pattern = "abc"
    expected = ""
    got = smallest_window_containing_substring(string, pattern)
    assert got == expected
