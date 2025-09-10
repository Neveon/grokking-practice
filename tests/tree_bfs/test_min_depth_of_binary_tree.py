import pytest
from patterns.tree_bfs.min_depth_of_binary_tree import min_depth
from tests.utils.tree import TreeNode


def test_example_1():
    # Build this tree:
    #            1
    #          /   \
    #         2     3
    #        / \
    #       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    expected = 2
    got = min_depth(root)
    assert got == expected


def test_example_2():
    # Build this tree:
    #            1
    #          /   \
    #         2     3
    #        /     /
    #       4     6
    #      /
    #     7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(7)

    expected = 3
    got = min_depth(root)
    assert got == expected

