import pytest
from patterns.tree_dfs.path_with_given_sequence import has_path
from tests.utils.tree import TreeNode

def test_example_1():
    # Build this tree:
    #            1
    #          /   \
    #         7     9
    #        / \   / \
    #       4   5 2   7
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)

    sequence = [1, 9, 2]
    got = has_path(root, sequence)
    expected =  True
    assert got == expected

def test_example_2():
    # Build this tree:
    #            12
    #          /   \
    #         7     1
    #          \   / \
    #           4 10  5
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    sequence = [12, 7, 4]
    got = has_path(root, sequence)
    expected = True
    assert got == expected

