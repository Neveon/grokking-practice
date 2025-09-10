import pytest
from patterns.tree_bfs.level_order_successor import successor
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

    given = 3
    expected = 4
    got = successor(root, given)
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

    given = 5
    expected = 6
    got = successor(root, given)
    assert got == expected
