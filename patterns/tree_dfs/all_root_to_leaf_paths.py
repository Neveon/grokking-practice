"""
EASY

Given a binary tree, return all root-to-leaf paths
"""
from tests.utils.tree import TreeNode

def find_paths(root):
    all_paths = []
    all_root_to_leaf_paths(root, [], all_paths)

    return all_paths

def all_root_to_leaf_paths(current_node: TreeNode | None, current_path: list[int], all_paths: list[list[int]]):
    if current_node is None:
        return

    # Append current node to current path list
    current_path.append(current_node.value)

    # if current path is a leaf, add the current path to all_paths
    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path)) # make a copy of current_path and append it

        # NOTE: if we don't make a copy, then each entry in all_paths points to the same address
        #   thus when backtracking, current_path.pop() ripples through and empties everything
    else:
        # traverse left side sub-tree
        all_root_to_leaf_paths(current_node.left, current_path, all_paths)

        # traverse right side sub-tree
        all_root_to_leaf_paths(current_node.right, current_path, all_paths)

    # Remove node when backtracking up the stack
    current_path.pop()

# Time Complexity O(N^2) in worst case
#   traversal = O(N)
#   path copying = can be O(N) per path

# Space Complexity O(N*LogN)
#   If a path ends at level h, then there are about 2^h nodes in the path (h starts at 0)
#   maximum path length (root → leaf) in a balanced binary tree is O(Log N)
#                                          ––––––––––––––––––––
#   In a binary tree, the number of leaves is always ≤ (N+1)/2 => N/2
# 
#   Ultimately, if we count the all_paths output, then in a balanced tree we can have up to N/2 leaves 
#       each with a path of length log N, so storing them is O(N log N)
