import pytest
from patterns.tree_dfs.binary_tree_path_sum import binary_tree_path_sum
from tests.utils.tree import TreeNode

def test_example_1():
    # Build this tree:
    #            1
    #          /   \
    #         2     3
    #        / \   / \
    #       4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    sum = 10
    got = binary_tree_path_sum(root, sum)
    expected = True # 1, 3, 6
    assert got == expected

def test_example_2():
    # Build this tree:
    #            12
    #          /   \
    #         7     1
    #          \   / \
    #           9 10  5
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    sum = 23
    got = binary_tree_path_sum(root, sum)
    expected = True # 12, 1, 10
    assert got == expected

def test_example_3():
    # Build this tree:
    #            12
    #          /   \
    #         7     1
    #          \   / \
    #           9 10  5
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    sum = 16
    got = binary_tree_path_sum(root, sum)
    expected = False
    assert got == expected
