"""
EASY

Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1: Full 3-level binary tree
BFS result: [[1], [2, 3], [4, 5, 6, 7]]
            1
          /   \
         2     3
        / \\   / \
       4   5 6   7


Example 2: 3-level tree but last level is not full
BFS result: [[1], [2, 3], [4, 5, 6]]

            1
          /   \
         2     3
        / \\   /
       4   5 6

SOLUTION

We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

1. Start by pushing the root node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
5. After removing each node from the queue, insert both of its children into the queue.
6. If the queue is not empty, repeat from step 3 for the next level.
"""
from tests.utils.tree import TreeNode
from collections import deque

def bfs(root: TreeNode|None) -> list[list[int]]:
    result = []
    if root is None:
        return result

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

        result.append(current_level)

    return result
