"""
EASY

Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first.
You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""
from collections import deque
from tests.utils.tree import TreeNode

def reverse_traversal(root: TreeNode | None) -> list[list[int]]:
    result = deque()

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        result.appendleft(current_level)

    return list(result)
