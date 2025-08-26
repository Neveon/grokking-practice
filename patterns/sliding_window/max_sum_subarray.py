"""
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

def find_max_sum_subarray(k, arr):
    maxSum = 0
    curSum = 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        curSum += arr[windowEnd]

        # Slide the window
        if windowEnd >= k - 1: # Since counting array starts at 0, we need to subtract 1 from k

            # Check if we have a new max sum subarray
            maxSum = max(curSum, maxSum)

            curSum -= arr[windowStart]
            windowStart += 1

    return maxSum
