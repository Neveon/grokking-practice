"""
MEDIUM

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.

Example

                1
              /   \
             7     9
                  / \
                 2   9
Output: 408
17 + 192 + 199

We need a current_path array to store all numbers of the current path

When we reach a leaf (node.left & node.right are None) -> register the current_path as a number

Each path returns its own sum which the the path's number

When we backtrack, current_path.pop() as we go up the call stack
"""
from tests.utils.tree import TreeNode

def sum_of_path_numbers(node: TreeNode | None) -> int:
    return dfs(node, 0, [])

def dfs(node: TreeNode | None, sum: int, current_path: list[int]) -> int:
    if node is None:
        return 0

    current_path.append(node.value)

    # found leaf, register number and add to sum
    if node.left is None and node.right is None:
        sum = path_to_number(current_path)
    else:
        sum = dfs(node.left, sum, current_path) + dfs(node.right, sum, current_path)

    # backtracking - remove last node as we go up the stack
    current_path.pop()

    return sum


def path_to_number(path: list[int]) -> int:
    num = 0

    for i in range(len(path)):
        order_of_magnitude = 10**(len(path) - i - 1)
        num += path[i] * order_of_magnitude

    return num
