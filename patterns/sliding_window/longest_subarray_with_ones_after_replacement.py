"""
HARD

-----------------
Problem Statement
-----------------
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

-----------------
Example 1:
-----------------
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

-----------------
Example 2:
-----------------
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

# Grokking Solution
def longest_subarray_with_ones_after_replacement(arr, k):
    window_start = 0
    max_length = 0
    max_ones_count = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # Current window size is (window_end - window_start + 1)
        # Which means we have a maximum number of 1s repeating in a given window
        # A window has 1 max_ones_count times and has a remainder of 0s which should be replaced with 1s
        # If the remaining 0s are >k then we need to shrink the window
        if window_end - window_start + 1 - max_ones_count > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


"""
My solution
def longest_subarray_with_ones_after_replacement(arr, k):
    window_start = 0
    max_length = 0
    zero_counter = 0

    for window_end in range(len(arr)):
        right_ptr = arr[window_end]
        if right_ptr == 0:
            zero_counter += 1
        # If we have >k number of 0s then we need to shrink the window
        if zero_counter > k:
            left_ptr = arr[window_start]
            # Check if window start is 0
            if left_ptr == 0:
                zero_counter -= 1
            # shrink window
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length
"""

