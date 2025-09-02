"""
MEDIUM

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

----------
Example 1:
----------
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

----------
Example 2:
----------
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

----------
Example 3:
----------
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

1. Sort the array in place (arr.sort())
2. Find triplet sums close to target - similar to triplet sum to zero problem
    target = x + y + z
3. Get sum of the elements of the triplet close to the target
4. Compare last triplet sum to current triplet sum to get closest sum
"""
import math

def triplet_sum_to_close_to_target(arr, target):
    arr.sort()
    closest_sum = math.inf

    for i in range(len(arr)):
        lo = i + 1
        hi = len(arr) - 1
        while lo < hi:
            cur_sum = arr[i] + arr[lo] + arr[hi]

            if abs(cur_sum - target) < abs(closest_sum - target):
                closest_sum = cur_sum

            if cur_sum == target:
                return cur_sum
            elif cur_sum < target:
                lo += 1
            else:
                hi -= 1

    return closest_sum
