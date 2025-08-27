import pytest
from patterns.sliding_window.string_anagrams import string_anagrams

def test_example_1():
    string="ppqp"
    pattern="pq"
    expected = [1, 2]
    got = string_anagrams(string, pattern)
    assert got == expected

def test_example_2():
    string="abbcabc"
    pattern="abc"
    expected = [2, 3, 4]
    got = string_anagrams(string, pattern)
    assert got == expected
