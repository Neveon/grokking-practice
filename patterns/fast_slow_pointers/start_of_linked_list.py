"""
MEDIUM

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

SOLUTION

1. Use fast, slow pointers to find the cycle - we know the slow pointer will be in the cycle
2. Once in the cycle, count how long the cycle is (until cur = slow)
3. Iterate through LL with two pointers. Pointer 2 will be equal to the length of the cycle. Pointer1++ & Pointer2++ until Pointer2.next == Pointer1
    Where Pointer1 lands is where the LL cycle starts
"""

def start_of_linked_list(head):
    # Step 1
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            # Step 2 Node(5)
            length_of_cycle = find_length(slow)
            return find_start(head, length_of_cycle)
    # No cycle
    return None

def find_length(slow):
    current = slow.next
    length_of_cycle = 1
    while current is not slow:
        current = current.next
        length_of_cycle += 1

    return length_of_cycle

# Step 3
def find_start(head, length_of_cycle):
    ptr1, ptr2 = head, head
    # ptr2 should be length_of_cycle ahead of ptr1
    for _ in range(length_of_cycle):
        ptr2 = ptr2.next

    while ptr1 is not ptr2:
        ptr2 = ptr2.next
        ptr1 = ptr1.next

    return ptr1
