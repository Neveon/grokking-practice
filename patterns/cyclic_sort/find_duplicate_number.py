"""
EASY

We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4

[1, 4, 4, 3, 2] i = 0 value = 1

[1, 4, 4, 3, 2] i = 1 value = 4

[1, 2, 4, 3, 4] i = 1 value = 2

[1, 2, 4, 3, 4] i = 2 value = 4

[1, 2, 3, 4, 4] i = 2 value = 3

[1, 2, 3, 4, 4] i = 3 value = 4

Check
    value - 1 != i
AND
    arr[i] != arr[value - 1]
"""
def find_duplicate_number(arr):
    i = 0
    while i < len(arr):
        value = arr[i]
        if value-1 != i:
            j = value - 1
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i] # swap
            else:
                return arr[i]
        else:
            i += 1

    return -1

# Time Complexity O(N)
# Space Complexity O(1) no extra space used
