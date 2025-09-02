"""
MEDIUM

Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.

----------
Example 1:
----------
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

----------
Example 2:
----------
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""

def triplets_with_smaller_sum(arr, target):
    arr.sort()
    smallest_triplets = 0

    for i in range(len(arr) - 2):
        lo = i + 1
        hi = len(arr) - 1

        while lo < hi:
            cur_sum = arr[i] + arr[lo] + arr[hi]

            if cur_sum < target:
                # cur_sum < target for all elems in [lo+1..hi]
                smallest_triplets += (hi - lo)
                lo += 1
            if cur_sum >= target:
                hi -= 1

    return smallest_triplets
