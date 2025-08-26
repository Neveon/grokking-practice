import pytest
from patterns.sliding_window.intro import find_avgs_of_subarray_optimal

def test_example_from_grokking():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    expected = [2.2, 2.8, 2.4, 3.6, 2.8]
    got = find_avgs_of_subarray_optimal(k, arr)
    assert len(got) == len(expected)
