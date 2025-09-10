"""
EASY

Find the minimum depth of a binary tree.
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""
from collections import deque
from tests.utils.tree import TreeNode

def min_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    min_depth = 1
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.left is None and current_node.right is None: # found the leaf
                return min_depth

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        min_depth += 1
    return -1
