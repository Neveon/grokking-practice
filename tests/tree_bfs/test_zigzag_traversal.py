import pytest
from patterns.tree_bfs.zigzag_traversal import zigzag_traversal, grokking_zigzag_traversal
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

    expected = [[1], [3, 2], [4, 5, 6, 7]]
    got = zigzag_traversal(root)
    assert got == expected


def test_example_2():
    # Build this tree:
    #            1
    #          /   \
    #         2     3
    #        / \   /
    #       4   5 6
    #      /     \
    #     7       8
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    expected = [[1], [3, 2], [4, 5, 6], [8, 7]]
    got = zigzag_traversal(root)
    assert got == expected


def test_example_3():
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

    expected = [[1], [3, 2], [4, 5, 6, 7]]
    got = grokking_zigzag_traversal(root)
    assert got == expected


def test_example_4():
    # Build this tree:
    #            1
    #          /   \
    #         2     3
    #        / \   /
    #       4   5 6
    #      /     \
    #     7       8
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    expected = [[1], [3, 2], [4, 5, 6], [8, 7]]
    got = grokking_zigzag_traversal(root)
    assert got == expected

