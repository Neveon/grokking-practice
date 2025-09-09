"""
EASY

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]

SOLUTION

range is from 1 to n which means n-1 should equal i

[3, 4, 4, 5, 5] i = 0 value = 3
is value-1 != i?
is arr[value-1] != arr[i] ? If its equal, it means we already have a duplicate in the right place

[4, 4, 3, 5, 5] i = 0 value = 4
[5, 4, 3, 4, 5] i = 0 value = 5
5 is not in the correct index AND 5 == 5 so we have a duplicate
- Add to the duplicate_numbers array and increment i

[5, 4, 3, 4, 5] i = 1 value = 4
4 is not in the correct index AND 4 == 4 so we have a duplicate
- Add to the duplicate_numbers array and increment i

[5, 4, 3, 4, 5] i = 2 value = 3
[5, 4, 3, 4, 5] i = 3 value = 4
[5, 4, 3, 4, 5] i = 4 value = 5

duplicate_numbers = [4, 5]
"""

# Time Complexity O(N)
# Space Complexity O(N-1) => O(N) worse case we have almost all duplicates
def find_all_duplicate_numbers(arr):
    duplicate_numbers = []
    i = 0

    while i < len(arr):
        j = arr[i] - 1
        # swap only if element isn't in correct (current) index AND element isn't already placed in the index it is supposed to be in
        if i != j and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        elif i != j and arr[i] == arr[j]:
            duplicate_numbers.append(arr[i])
            i += 1
        else:
            i += 1

    return duplicate_numbers

# Grokking Solution
def grokking_find_all_duplicate_numbers(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i] # swap
        else:
            i += 1

    duplicate_numbers = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            duplicate_numbers.append(arr[i])

    return duplicate_numbers
