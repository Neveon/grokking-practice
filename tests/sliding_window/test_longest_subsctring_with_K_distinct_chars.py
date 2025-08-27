import pytest
from patterns.sliding_window.longest_substring_with_K_distinct_chars import longest_substring_with_K_distinct_chars

def test_example_1():
    string = "araaci"
    k = 2
    expected = 4
    got = longest_substring_with_K_distinct_chars(string, k)
    assert got == expected

def test_example_2():
    string = "araaci"
    k = 1
    expected = 2
    got = longest_substring_with_K_distinct_chars(string, k)
    assert got == expected

def test_example_3():
    string = "cbbebi"
    k = 3
    expected = 5
    got = longest_substring_with_K_distinct_chars(string, k)
    assert got == expected
