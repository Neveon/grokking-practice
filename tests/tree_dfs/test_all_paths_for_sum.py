import pytest
from patterns.tree_dfs.all_paths_for_sum import all_paths_for_sum
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

    sum = 12
    got = all_paths_for_sum(root, sum)
    # 1, 7, 4
    # 1, 9 ,2
    expected =  2
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

    sum = 23
    got = all_paths_for_sum(root, sum)
    # 12, 7, 4
    # 12, 1, 10
    expected = 2
    assert got == expected
