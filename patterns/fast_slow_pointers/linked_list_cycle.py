"""
EASY

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""

def linked_list_cycle(head):
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False

# For both problems:
# Time Complexity O(N)
# Space Complexity O(1)

"""
EASY

Given the head of a LinkedList with a cycle, find the length of the cycle.

Solution: 
    We can use the above solution to find the cycle in the LinkedList.
    Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to find the length of the cycle.
"""
def find_length_of_cycle(head):
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return calc_cycle_length(slow)

    return 0

def calc_cycle_length(slow):
    current = slow.next
    cycle_length = 1

    while current != slow:
        cycle_length += 1
        current = current.next

    return cycle_length
