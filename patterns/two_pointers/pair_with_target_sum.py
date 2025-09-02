"""
EASY

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

----------
Example 1:
----------
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

----------
Example 2:
----------
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

Brute Force Method:
    Since the given array is sorted, a brute-force solution could be to iterate through the array, taking one number at a time and searching for the second number through Binary Search. 
    The time complexity of this algorithm will be O(N∗logN). Can we do better than this?
"""

def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        
        if target > current_sum:
            left += 1 # we need a pair with a bigger sum
        else:
            right -= 1 # we need a pair with a smaller sum
    return [-1, -1]

# Time Complexity O(N)
# Space Complexity O(1)

"""
An Alternate approach #
Instead of using a two-pointer or a binary search approach, we can utilize a HashTable to search for the required pair. 
We can iterate through the array one number at a time. 
Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ such that “X+Y==Target”. 

We will do two things here:

Search for ‘Y’ (which is equivalent to “Target − X”) in the HashTable. If it is there, we have found the required pair.
Otherwise, insert “X” in the HashTable, so that we can search it for the later numbers.
Here is what our algorithm will look like:
"""

def alt_pair_with_target_sum(arr, target):
    past_nums = {} # store numbers and their indices
    for idx, num in enumerate(arr):
        if target - num in past_nums:
            return [past_nums[target - num], idx]
        else:
            past_nums[arr[idx]] = idx
    return [-1, -1]

# Time Complexity O(N)
# Space Complexity O(N)
