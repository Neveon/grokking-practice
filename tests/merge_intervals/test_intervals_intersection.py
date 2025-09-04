import pytest
from patterns.merge_intervals.intervals_intersection import  intervals_intersection
from tests.utils.interval import Interval

def test_example_1():
    intervals_1 = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
    intervals_2 = [Interval(2, 3), Interval(5, 7)]
    expected = [Interval(2, 3), Interval(5, 6), Interval(7, 7)]
    got = intervals_intersection(intervals_1, intervals_2) 
    assert got == expected

def test_example_2():
    intervals_1 = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
    intervals_2 = [Interval(5, 10)]
    expected = [Interval(5, 7), Interval(9, 10)]
    got = intervals_intersection(intervals_1, intervals_2) 
    assert got == expected
