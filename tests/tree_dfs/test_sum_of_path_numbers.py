import pytest
from patterns.tree_dfs.sum_of_path_numbers import sum_of_path_numbers
from tests.utils.tree import TreeNode

def test_example_2():
    # Build this tree:
    #            1
    #          /   \
    #         7     9
    #              / \
    #             2   9
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)

    got = sum_of_path_numbers(root)
    expected = 408
    assert got == expected

def test_example_3():
    # Build this tree:
    #            8
    #          /   \
    #         7     1
    #          \   / \
    #           9 1   5
    root = TreeNode(8)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    got = sum_of_path_numbers(root)
    expected = 2505
    assert got == expected
