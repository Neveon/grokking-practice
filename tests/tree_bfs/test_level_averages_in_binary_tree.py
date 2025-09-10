import pytest
from patterns.tree_bfs.level_averages_in_binary_tree import level_averages
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

    expected = [1, 2.5, 5.5]
    got = level_averages(root)
    assert got == expected


def test_example_2():
    # Build this tree:
    #            1
    #          /   \
    #         2     3
    #        / \   /
    #       4   5 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    expected = [1, 2.5, 5]
    got = level_averages(root)
    assert got == expected

