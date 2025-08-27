import pytest
from patterns.sliding_window.longest_substring_with_same_letters_after_replacement import longest_substring_with_same_letters_after_replacement 

def test_example_1():
    string = "aabccbb"
    k = 2
    expected = 5
    got = longest_substring_with_same_letters_after_replacement(string, k)
    assert got == expected

def test_example_2():
    string = "abbcb"
    k = 1
    expected = 4
    got = longest_substring_with_same_letters_after_replacement(string, k)
    assert got == expected

def test_example_3():
    string = "abccde"
    k = 1
    expected = 3
    got = longest_substring_with_same_letters_after_replacement(string, k)
    assert got == expected
