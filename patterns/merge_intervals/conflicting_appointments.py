"""
MEDIUM

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

SOLUTION

Sort intervals
Appointments: [[4,5], [2,3], [3,6]]
=> [[2,3], [3,6], [4,5]]

Initiate two pointers

Does int1 overlap with int2?

    int2.start < int1.end < int2.end

    int2.start < int1.end > int2.end

In either above case we only need to check if the next interval starts within the previous interval
    int2.start < int1.end

"""

from tests.utils.interval import Interval

def can_attend_all_appointments(intervals: list[Interval]) -> bool:
    if len(intervals) == 1:
        return True

    # Sort intervals by start time - O(N Log N)
    intervals.sort(key = lambda x: x.start)

    for j in range(1, len(intervals)):
        prev_interval = intervals[j-1]
        cur_interval = intervals[j]

        if cur_interval.start < prev_interval.end:
            return False

    return True

