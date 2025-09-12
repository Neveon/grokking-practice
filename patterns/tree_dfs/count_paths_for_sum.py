"""
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

SOLUTION

This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. But there will be four differences:

1. We will keep track of the current path in a list which will be passed to every recursive call.

2. Whenever we traverse a node we will do two things:
    - Add the current node to the current path.
    - As we added a new node to the current path, we should find the sums of all sub-paths ending at the current node.
        If the sum of any sub-path is equal to ‘S’ we will increment our path count.

3. We will traverse all paths and will not stop processing after finding the first path.

4. Remove the current node from the current path before returning from the function.
    This is needed to Backtrack while we are going up the recursive call stack to process other paths.

"""
from tests.utils.tree import TreeNode

def count_paths(root: TreeNode | None, S: int):
    all_paths = []
    return count_paths_recursive(root, S, all_paths)

def count_paths_recursive(node: TreeNode | None, S: int, current_path: list):
    if node is None:
        return 0

    # add current node to the path
    current_path.append(node.value)

    path_count, path_sum = 0, 0
    # find sum of all sub-paths in the current_path list
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count
        if path_sum == S:
            path_count += 1

    # traverse left sub-tree
    path_count += count_paths_recursive(node.left, S, current_path)

    # traverse right sub-tree
    path_count += count_paths_recursive(node.right, S, current_path)

    # remove current_node from current_path as we backtrack and go up the call stack
    current_path.pop()

    return path_count

# Time Complexity O(N^2) worst case otherwise O(NLogN) in balanced tree
#   where H = N in a skewed tree (Singly Linked List) or H = LogN in a balanced tree
# Space Complexity O(H)
#   where H = N in a skewed tree (Singly Linked List) or H = LogN in a balanced tree

"""
OPTIMIZED SOLUTION

Use prefix sum (Range Sum) to get O(N) time to find sum
https://www.youtube.com/watch?v=xbYr9JOC2Lk

A prefix sum is the cumulative sum of values from the root down to the current node.
	• Example path: 12 → 7 → 4
	• Prefix sums = [12, 19, 23]

    Example if s = 11 and current_node = 4
    Our current sum would be 23, we add to count of valid subpaths with current_sum - target (23 - 11)
    prefix_sum has a 12 -> therefore we have a valid subpath

Time Complexity O(N)
Space Complexity O(H) where H = N in singly Linked List or H = LogN in a balanced tree
"""
def optimized_count_paths(root: TreeNode | None, target: int) -> int:
    # hashmap stores {prefix_sum: frequency}
    prefix_map = {0: 1}  # if current_sum - target = 0 (essentially root to node), then it is counted
    return _dfs(root, 0, target, prefix_map)


def _dfs(node: TreeNode | None,
         current_sum: int,
         target: int,
         prefix_map: dict[int, int]) -> int:

    if node is None:
        return 0

    # Update current prefix sum
    current_sum += node.value

    # Count valid subpaths ending here
    count = prefix_map.get(current_sum - target, 0)

    # Add this prefix sum to map
    prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    # Recurse children
    count += _dfs(node.left, current_sum, target, prefix_map)
    count += _dfs(node.right, current_sum, target, prefix_map)

    # Backtrack: remove this prefix sum
    prefix_map[current_sum] -= 1
    if prefix_map[current_sum] == 0:
        del prefix_map[current_sum]

    return count

