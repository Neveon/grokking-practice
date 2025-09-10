"""
MEDIUM

Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
"""
from collections import deque
from tests.utils.tree import TreeNode

def connect_level_order_siblings(root: TreeNode) -> list[list[int]]:
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level = []
        prev_node = None

        for _ in range(level_size):
            current_node = queue.popleft()

            if prev_node is not None:
                prev_node.next = current_node
            prev_node = current_node

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

            level.append(current_node.value)
        
        result.append(level)

    return result

def grokking_solution(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    while queue:
        prev_node = None
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()
            if prev_node:
                prev_node.next = current_node
            prev_node = current_node

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
