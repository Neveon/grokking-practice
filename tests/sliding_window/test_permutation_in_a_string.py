import pytest
from patterns.sliding_window.permutation_in_a_string import permutation_in_a_string

def test_example_1():
    string = "oidbcaf"
    pattern = "abc"
    expected = True
    got = permutation_in_a_string(string, pattern)
    assert expected == got

def test_example_2():
    string = "odicf"
    pattern = "dc"
    expected = False
    got = permutation_in_a_string(string, pattern)
    assert expected == got

def test_example_3():
    string = "bcdxabcdy"
    pattern = "bcdyabcdx"
    expected = True
    got = permutation_in_a_string(string, pattern)
    assert expected == got

def test_example_4():
    string = "aaacb"
    pattern = "abc"
    expected = True
    got = permutation_in_a_string(string, pattern)
    assert expected == got
