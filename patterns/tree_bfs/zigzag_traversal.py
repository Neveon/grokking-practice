"""
MEDIUM

Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

Example 1: Full 3-level binary tree
ZigZag result: [[1], [3, 2], [4, 5, 6, 7]]
            1
          /   \
         2     3
        / \\   / \
       4   5  6   7

Example 2: 3-level tree but last level is not full
ZigZag result: [[1], [3, 2], [4, 5, 6], [8, 7]]

            1
          /   \
         2     3
        / \\   /
       4   5  6
      /     \\
     7       8 
"""
from collections import deque
from tests.utils.tree import TreeNode

def zigzag_traversal(root: TreeNode | None) -> list[list[int]]:
    result = []

    queue = deque()
    queue.append(root)
    i = 1
    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            current_node = queue.popleft()
            if i % 2 == 0:
                current_level.appendleft(current_node.value)
            else:
                current_level.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        result.append(list(current_level))
        i += 1

    return result

# Grokking Solution
def grokking_zigzag_traversal(root: TreeNode | None) -> list[list[int]]:
    result = []

    queue = deque()
    queue.append(root)
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            current_node = queue.popleft()
            if left_to_right:
                current_level.append(current_node.value)
            else:
                current_level.appendleft(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        result.append(list(current_level))
        left_to_right = not left_to_right

    return result
