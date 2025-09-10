"""
EASY

Given a binary tree, populate an array to represent the averages of all of its levels.
"""
from collections import deque
from tests.utils.tree import TreeNode

def level_averages(root: TreeNode | None) -> list[list[int]]:
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        sum = 0

        for _ in range(level_size):
            current_node = queue.popleft()
            sum += current_node.value
            
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        result.append(sum / level_size)

    return result
