import pytest
from patterns.merge_intervals.conflicting_appointments import can_attend_all_appointments
from tests.utils.interval import Interval

def test_example_1():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    expected = False
    got = can_attend_all_appointments(intervals) 
    assert got == expected


def test_example_2():
    intervals = [Interval(6, 7), Interval(2, 4), Interval(8, 12)]
    expected = True
    got = can_attend_all_appointments(intervals) 
    assert got == expected


def test_example_3():
    intervals = [Interval(4, 5), Interval(2, 3), Interval(3, 6)]
    expected = False
    got = can_attend_all_appointments(intervals) 
    assert got == expected


