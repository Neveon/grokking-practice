import pytest
from patterns.sliding_window.words_concatenation import words_concatenation

def test_example_1():
    string = "catfoxcat"
    words = ["cat", "fox"]
    expected = [0, 3]
    got = words_concatenation(string, words)
    assert got == expected

def test_example_2():
    string = "catcatfoxfox"
    words = ["cat", "fox"]
    expected = [3]
    got = words_concatenation(string, words)
    assert got == expected
