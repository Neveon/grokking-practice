"""
MEDIUM

Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.

SOLUTION

Use two pointers for each array of intervals which are already sorted
    int1 & int2

Check if any of the intervals overlap and take the min(int.end) and max(int.start)

1. int2 start time lies within int1
    int1.start <= int2.start <= int1.end

2. int1 start time lies within int2
    in2.start <= int1.start <= int2.end

"""
from tests.utils.interval import Interval

def intervals_intersection(intervals1: list[Interval], intervals2: list[Interval]) -> list[Interval]:
    common_intervals = []

    # The intervals are already sorted
    # Init two pointers
    int1 = 0
    int2 = 0

    while int1 < len(intervals1) and int2 < len(intervals2):
        interval_1 = intervals1[int1]
        interval_2 = intervals2[int2]

        # Check if any of the intervals overlap
        if interval_1.start <= interval_2.start and interval_2.start <= interval_1.end or \
        interval_2.start <= interval_1.start and interval_1.start <= interval_2.end:
            common_start = max(interval_2.start, interval_1.start)
            common_end = min(interval_2.end, interval_1.end)
            common_intervals.append(Interval(common_start, common_end))

        # Increment pointer depending on the interval which ends first
        if interval_1.end < interval_2.end:
            int1 += 1
        else:
            int2 += 1

    return common_intervals
