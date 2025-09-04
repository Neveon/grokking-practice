"""
MEDIUM

Given a list of non-overlapping intervals sorted by their start time, insert a given interval 
at the correct position and merge all necessary intervals to produce a list that has only 
mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

SOLUTION

If the given list was not sorted, we could have simply appended the new interval to it and used the merge() function from Merge Intervals.
But since the given list is sorted, we should try to come up with a solution better than 
O(N∗logN)

When inserting a new interval in a sorted list, we need to first find the correct index where the new interval can be placed. 
In other words, we need to skip all the intervals which end before the start of the new interval. So we can iterate through the given sorted listed of intervals and skip all the intervals with the following condition:

intervals[i].end < new_interval.start
Once we have found the correct place, we can follow an approach similar to Merge Intervals to insert and/or merge the new interval.

We need to do something like this:
    c.start = min(a.start, b.start)
    c.end = max(a.end, b.end)

Our overall algorithm will look like this:

1. Skip all intervals which end before the start of the new interval, i.e., skip all intervals with the following condition:
    intervals[i].end < newInterval.start

2. Let’s call the last interval ‘b’ that does not satisfy the above condition. If ‘b’ overlaps with the new interval (a) (i.e. b.start <= a.end), we need to merge them into a new interval ‘c’:
    c.start = min(a.start, b.start)
    c.end = max(a.end, b.end)

3. We will repeat the above two steps to merge ‘c’ with the next overlapping interval.
"""
from tests.utils.interval import Interval

# In Python 3.9+ we can specify types without needing to import typing

# intervals is already sorted
# intervals should have mutually exclusive intervals already, when inserting we only merge new_interval
def insert_interval(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    merged = []
    i= 0

    # start (and add to output) all intervals that come before the 'new_interval' start
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1

    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged
