"""
MEDIUM

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

head -> 2 -> 4 -> 6 -> 8 -> 10 -> null

null <- 2 <- 4 <- 6 <- 8 <- 10 <- head

SOLUTION
The problem follows the In-place Reversal of a LinkedList pattern.
We can use a similar approach as discussed in Reverse a LinkedList.
Here are the steps we need to follow:

1. Skip the first p-1 nodes, to reach the node at position p.
2. Remember the node at position p-1 to be used later to connect with the reversed sub-list.
3. Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
4. Connect the p-1 and q+1 nodes to the reversed sub-list.

"""
def reverse_sub_list(head, p, q):
    if p == q:
        return head

    # after skipping 'p-1' nodes, current will point to 'p'th node
    previous, current = None, head
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # we are interested in three parts of the LinkedList
    # 1. The part before index 'p'
    # 2. The part between 'p' and 'q'
    # 3. The part after index 'q'
    last_node_of_first_part = previous

    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None # will be used to temporarily store the next node

    i = p
    # reverse nodes between 'p' and 'q' (inclusive of q)
    while current is not None and i <= q:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect with the first part
    if last_node_of_first_part is not None:
        # 'previous' is now the first node of the sub-list
        last_node_of_first_part.next = previous
    # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
    else:
        head = previous

    # connect with the last part
    last_node_of_sub_list.next = current
    return head

# Time Complexity O(N)
# Space Complexity O(1) constant space
