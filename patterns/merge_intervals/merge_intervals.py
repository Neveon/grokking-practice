"""
MEDIUM

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.


Given two intervals (a & b), there will be SIX different ways the two intervals can relate to each other:

    1. [a][b]           => a & b do not overlap

    2. [a1, b2][b3]      => a & b overlap, where b ends after a

    3. [a1, b2, b3, a4] => a completely overlaps b

    4. [b1, a2][a3]      => a & b overlap, where a ends after b

    5. [b1, a2, a3, b4] => b completely overlaps a

    6. [b][a]           => a & b do not overlaps

# Note: a&b can have cases where they can have the same start and/or end times as well.
    Not sure why Grokking didn't include those options. These are general ways two intervals can relate.

SOLUTION

1. Sort the intervals on the start time to ensure a.start <= b.start
2. If ‘a’ overlaps ‘b’ (i.e. b.start <= a.end), we need to merge them into a new interval ‘c’ such that:
    c.start = a.start
    c.end = max(a.end, b.end)
3. We will keep repeating the above two steps to merge ‘c’ with the next interval if it overlaps with ‘c’.
"""
from tests.utils.interval import Interval

def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals

    # Step 1 - sort intervals on the start time
    intervals.sort(key = lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end: # overlapping intervals, adjust 'end'
            end = max(interval.end, end)
        else: # non-overlapping interval, add the previous interval and reset
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    merged_intervals.append(Interval(start, end))
    return merged_intervals

# Time Complexity O(N Log N) since we have to sort the intervals by the start interval
# Space Complexity O(N) worse case
