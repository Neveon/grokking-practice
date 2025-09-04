"""
EASY

We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2

Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

SOLUTION

1. Cyclic Sort
Numbers start at 0.
Since there will be a missing number, there will be a number found in the array which is equal to the len(arr)

We cannot place this number in the correpsonding index since there won't be a place for it, we will have to ignore it

2. Iterate through after sorting in place to find missing number
"""

def find_missing_number(arr):
    i = 0
    while i < len(arr):
        num = arr[i]
        # Ensure number is in array 0-index count and is in correct index
        if num < len(arr) and num != i:
            arr[i], arr[num] = arr[num], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        num = arr[i]
        if num != i:
            return i

# Time Complexity O(N)
# Space Complexity O(1) we don't use extra space
