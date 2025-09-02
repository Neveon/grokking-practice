"""
EASY

Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the new length of the array.

----------
Example 1:
----------
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

----------
Example 2:
----------
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

SOLUTION
We need to remove the duplicates in-place such that the resultant length of the array remains sorted.
As the input array is sorted, one way to do this is to shift the elements left whenever we encounter duplicates.
In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number.
So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.
"""

def remove_duplicates(arr):
    if not arr:
        return 0

    # index of the position where the next unique element should be placed
    # The first element (arr[0]) is always unique in a sorted array.
    cur_unique_elem = 0   # last unique element index

    for next in range(len(arr)):
        # compare next elem to current unique element
        if arr[next] != arr[cur_unique_elem]:
            # If they're not equal then the index of cur_unique_elem + 1
            # is the new cur_unique_elem which is the 'next' elem
            cur_unique_elem += 1
            arr[cur_unique_elem] = arr[next]

    return cur_unique_elem + 1 # index is off by 1 count

# Time Complexity O(N)
# Space Complexity O(1) - we don't use any extra space

"""
EASY

Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

----------
Example 1:
----------
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

----------
Example 2:
----------
Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].

Solution: This problem is quite similar to our parent problem. We can follow a two-pointer approach and shift numbers left upon encountering the ‘key’.

Here is what the code will look like:
"""

def remove_key_duplicates(arr, key):
    next_none_key = 0

    for elem in arr:
        if elem != key:
            arr[next_none_key] = elem
            next_none_key += 1

    return next_none_key
