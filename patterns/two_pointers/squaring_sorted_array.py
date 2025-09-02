"""
EASY

Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

----------
Example 1:
----------
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

----------
Example 2:
----------
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""

def squaring_sorted_array(arr):
    # Init new array of length arr
    res = [0] * len(arr)
    # Keep a pointer to the last index to fill in the new array
    next_largest = len(res) - 1

    left = 0
    right = len(arr) - 1

    # <= because if odd number of elements, we need to still compare the middle number
    while left <= right:
        left_elem_sq = arr[left] * arr[left]
        right_elem_sq = arr[right] * arr[right]

        # compare absolute value squared, whatever is largest is the next_largest
        if abs(left_elem_sq) > abs(right_elem_sq):
            res[next_largest] = left_elem_sq
            left += 1
        else:
            res[next_largest] = right_elem_sq
            right -= 1

        next_largest -= 1

    return res

# Time Complexity O(N)
# Space Complexity O(N)
