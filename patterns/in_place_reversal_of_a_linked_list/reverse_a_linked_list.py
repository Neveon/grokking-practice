"""
EASY

Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.

head -> 2 -> 4 -> 6 -> 8 -> 10 -> null

null <- 2 <- 4 <- 6 <- 8 <- 10 <- head

SOLUTION

To reverse a LinkedList, we need to reverse one node at a time.
We will start with a variable current which will initially point to the head of the LinkedList and a variable previous which will point to the previous node that we have processed; initially previous will point to null.

In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on to the next node. 
Also, we will update the previous to always point to the previous node that we have processed.
"""
from tests.utils.linked_list_utils import Node

def reverse_linked_list(head: Node):
    prev, cur, next = None, head, None

    while cur is not None:
        next = cur.next # temporarily store the next node
        cur.next = prev # reverse the cur node
        prev = cur # before we move to the next node, point prev to the current node
        cur = next
    return prev

# Time Complexity O(N)
# Space Complexity O(1)
