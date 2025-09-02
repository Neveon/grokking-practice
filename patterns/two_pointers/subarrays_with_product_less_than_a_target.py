"""
MEDIUM

Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

NOTE: “Contiguous subarrays” means we keep the original order and pick consecutive elements; sorting would destroy contiguity.

----------
Example 1:
----------
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

----------
Example 2:
----------
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""
def subarrays_with_product_less_than_a_target(arr, target):
    result = []
    product = 1 # track product
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        # Check if product is too high and make sure left side of window doesn't pass right
        while product >= target and left <= right:
            product = product // arr[left]
            left += 1

        # since the product of all numbers from left to right is < the target
        # all subarrays from left to right will have a product less than the target too.
        for start in range(left, right + 1):
            # slice creates the contiguous subarray ending at right
            result.append(arr[start:right + 1])
    return result

# Time Complexity  O(N^2)
#   worst case is we append up to ~n subarrays per right
# Space Complexity O(N^2)
#   worst case is we append up to ~n subarrays per right
