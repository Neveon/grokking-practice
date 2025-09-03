"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
"""

# Solution 1 - Counting
# Time Complexity O(N)
# Space Complexity O(1)
def middle_of_linked_list(head):
    if head is None:
        return 0

    length = 1
    while head is not None:
        head = head.next
        length += 1

    if length % 2 == 0:
        return length // 2
    else:
        return (length // 2) + 1

# Solution 2 - Fast/Slow Pointer
# Time Complexity O(N)
# Space Complexity O(1)
def middle_of_linked_list_fast_slow(head):
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    if fast is None:
        return slow.next
    else:
        return slow
