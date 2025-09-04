"""
EASY

We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
The array can have duplicates, which means some numbers will be missing.
Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:

Input: [2, 4, 1, 2]
Output: 3

Example 3:

Input: [2, 3, 2, 1]
Output: 4

SOLUTION

    Check if current pointer [i]'s value is in correct index

Iterate through and count all missing numbers where number-1 != index
"""

def find_all_missing_numbers(arr: list[int]) -> list[int]:
    i = 0
    missing_numbers = []

    while i < len(arr):
        value = arr[i]
        if value != arr[value-1]:
            arr[i], arr[value-1] = arr[value-1], arr[i]
        else:
            i += 1

    i = 0
    while i < len(arr):
        num = arr[i]
        if num - 1 != i:
            missing_numbers.append(i + 1)
        i += 1

    return missing_numbers

# Time Complexity O(N)
# Space Complexity O(1) we don't use any extra space
