"""
MEDIUM

-----------------
Problem Statement
-----------------
Given an array of characters where each character represents a fruit tree, you are given two baskets 
and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

-----------
Example 1:
-----------
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

-----------
Example 2:
-----------
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

# The key in this problem is that we need to stop when we need to pick from a third fruit type
# This makes it similar to the longest substring with K distinct characters problem
# In this case, k = 2
def fruits_into_baskets(arr):
    window_start = 0
    max_length = 0
    basket = dict()

    # Expand window
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        # Add fruit to basket
        if right_char not in basket:
            basket[right_char] = 0
        basket[right_char] += 1

        # If we have more than 2 fruit types, we need to shrink the window until we only have 2 fruit types
        while len(basket) > 2:
            left_char = arr[window_start]
            basket[left_char] -= 1
            # If the fruit type is 0 in the basket, delete it
            if basket[left_char] == 0:
                del basket[left_char]
            # Shrink the window
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# Time Complexity O(N)
# Space Complexity O(1) since k always is 2
