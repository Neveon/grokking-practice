"""
EASY

Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
import math

def smallest_subarray_with_given_sum(inp_arr, s):
    # Dynamic Window
    # Check len of window only when the elements are >= s
    # Shrink window start after above ^ AND if len of window is smaller while elems >= s, check the len continously
    window_start = 0
    window_sum = 0
    min_len = math.inf

    for window_end in range (len(inp_arr)):
        window_sum += inp_arr[window_end]

        # shrink the window as small as possible until window_sum is smaller than s
        while window_sum >= s:
            min_len = min(min_len, window_end - window_start + 1)
            window_sum -= inp_arr[window_start]
            window_start += 1

    if min_len == math.inf:
        return 0
    else:
        return min_len

# Time Complexity O(N + N) => O(2N) => O(N)
# Space Complexity O(1)
