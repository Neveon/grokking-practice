"""
MEDIUM

Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

k = 3
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null

Output: 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> null

1. Reverse sublist until the kth node (inclusive)
2. Repeat 1, until we hit null

In reversing a sublist there are 3 parts we need to connect
1. The part before the sublist
2. The sublist (reversed)
3. The part after the sublist
"""
def reverse_every_k_element_sublist(head, k):
    if k <= 1 or head is None:
        return head

    previous = None
    current = head
    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current # we know the first node in a sublist witll be the last node after reversal
        next = None

        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        last_node_of_sub_list.next = current

        # Since we swapped where the head and tail is for the sublist
        # Update the previous node to be the last node of the new sublist
        previous = last_node_of_sub_list

        # Check if we are at end of LinkedList
        if current is None:
            break
    return head
