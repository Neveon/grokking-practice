"""
MEDIUM

Given a binary tree and a number ‘S’, find and return the number of paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""
from tests.utils.tree import TreeNode

def all_paths_for_sum(root: TreeNode | None, sum: int):
    if root is None:
        return 0

    if root.value == sum and root.left is None and root.right is None:
        return 1

    return all_paths_for_sum(root.left, sum - root.value) + all_paths_for_sum(root.right, sum - root.value)

# Time Complexity O(N) we visit every node
# Space Complexity O(N) worst case if the tree is a Linked List (every node has a single child)
