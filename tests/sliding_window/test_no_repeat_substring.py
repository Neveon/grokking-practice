import pytest
from patterns.sliding_window.no_repeat_substring import no_repeat_substring

def test_example_1():
    string = "aabccbb"
    expected = 3
    got = no_repeat_substring(string)
    assert expected == got

def test_example_2():
    string = "abbbb"
    expected = 2
    got = no_repeat_substring(string)
    assert expected == got

def test_example_3():
    string = "abccde"
    expected = 3
    got = no_repeat_substring(string)
    assert expected == got
