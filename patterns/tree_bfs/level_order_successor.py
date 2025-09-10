"""
EASY

Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right after the given node in the level order traversal.
"""
from collections import deque
from tests.utils.tree import TreeNode

def successor(root: TreeNode | None, given: int) -> int:
    if root is None:
        return -1

    queue = deque()
    queue.append(root)

    is_next = False
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            if is_next:
                return current_node.value

            if current_node.value == given:
                is_next = True

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    return -1
