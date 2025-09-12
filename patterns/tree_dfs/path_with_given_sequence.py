"""
MEDIUM

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""
from tests.utils.tree import TreeNode

def has_path(root: TreeNode | None, sequence: list[int]) -> bool:
    if root is None:
        return len(sequence) == 0

    return has_path_recursive(root, sequence, 0)

def has_path_recursive(current_node: TreeNode | None, sequence: list[int], seq_index: int) -> bool:
    if current_node is None:
        return False

    seq_length = len(sequence)
    if seq_index >= len(sequence) or current_node.value != sequence[seq_index]:
        return False

    # if the current node is a leaf, add it is the end of the sequence, we have found a path!
    if current_node.left is None and current_node.right is None and current_node.value == sequence[seq_index]:
        return True

    # recursively call to traverse the left and right sub-tree
    # return True if any of the two recursive call return True
    return has_path_recursive(current_node.left, sequence, seq_index + 1) or has_path_recursive(current_node.right, sequence, seq_index + 1)

# Time Complexity O(N) worst case we go through all nodes
# Space Complexity O(N) worst case singly Linked List
