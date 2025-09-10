import pytest
from patterns.tree_bfs.reverse_level_order_traversal import reverse_traversal
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

    expected = [[4, 5, 6, 7], [2, 3], [1]]
    got = reverse_traversal(root)
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

    expected = [[4, 5, 6], [2, 3], [1]]
    got = reverse_traversal(root)
    assert got == expected

