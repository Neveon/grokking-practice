import pytest
from patterns.merge_intervals.merge_intervals import merge_intervals
from tests.utils.interval import Interval

def test_example_1():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    expected = [Interval(1, 5), Interval(7, 9)]
    got = merge_intervals(intervals) 
    assert got == expected


def test_example_2():
    intervals = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
    expected = [Interval(2, 4), Interval(5, 9)]
    got = merge_intervals(intervals) 
    assert got == expected


def test_example_3():
    intervals = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
    expected = [Interval(1, 6)]
    got = merge_intervals(intervals) 
    assert got == expected
