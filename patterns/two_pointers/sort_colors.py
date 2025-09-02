"""
MEDIUM

Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]


SOLUTION
The best sorting algorithm isn't Dutch National Flag - because it goes through the array twice.
It is Count Sort, it goes through the array once.

https://www.youtube.com/watch?v=1DJ2kGoNPWQ

For this problem, since we need to treat the numbers of the array as objects, we cannot use count sort
"""

def sort_colors(arr):
    low, mid, high = 0, 0, len(arr) - 1

    # if mid is 0, switch with low pointer
    # if mid is 1, then increment mid
    # if mid is 2, switch with high pointer
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
