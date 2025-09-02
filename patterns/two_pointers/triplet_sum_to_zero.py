"""
MEDIUM

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

----------
Example 1:
----------
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

----------
Example 2:
----------
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""

def triplet_sum_to_zero(arr):
    # sort the array O(N Log N)
    arr.sort() # sorts in place (NOTE: sorted(arr) sorts and returns a new array)
    triplets = []
    for i in range (len(arr)):
        # skip same element to avoid duplicate triplets, we only want unique triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)

    return triplets

def search_pair(arr, target_sum, lo, triplets):
    hi = len(arr) - 1
    while (lo < hi):
        cur_sum = arr[lo] + arr[hi]
        if cur_sum == target_sum: # found the triplet
            triplets.append([-target_sum, arr[lo], arr[hi]])
            lo += 1
            hi -= 1

             # skip same elem to avoid duplicate triplets
            while lo < hi and arr[lo] == arr[lo - 1]:
                lo += 1
            while lo < hi and arr[hi] == arr[hi + 1]:
                hi -= 1
        
        elif target_sum > cur_sum:
            lo += 1 # we need a pair with a bigger sum
        else:
            hi -= 1 # we need a pair with a smaller sum

# Time Complexity O(N^2)
#   sorting will take O(N * logN) and search_pair() for every number in the array is O(N^2)
# O(N * logN + N^2) => asymptotically equivalent to O(N^2)

# Space Complexity O(N)
# Ignoring space required for output array, sorting itself will require O(N) space worse case
