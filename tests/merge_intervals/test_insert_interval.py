import pytest
from patterns.merge_intervals.insert_interval import insert_interval
from tests.utils.interval import Interval

def test_example_1():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    new_interval = Interval(4, 6)
    expected = [Interval(1, 3), Interval(4, 7), Interval(8, 12)]
    got = insert_interval(intervals, new_interval) 
    assert got == expected


def test_example_2():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    new_interval = Interval(4, 10)
    expected = [Interval(1, 3), Interval(4, 12)]
    got = insert_interval(intervals, new_interval) 
    assert got == expected


def test_example_3():
    intervals = [Interval(2, 3), Interval(5, 7)]
    new_interval = Interval(1, 4)
    expected = [Interval(1, 4), Interval(5, 7)]
    got = insert_interval(intervals, new_interval) 
    assert got == expected

