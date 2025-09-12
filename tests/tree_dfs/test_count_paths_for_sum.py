import pytest
from patterns.tree_dfs.count_paths_for_sum import count_paths, optimized_count_paths
from tests.utils.tree import TreeNode

def test_example_1():
    # Build this tree:
    #            1
    #          /   \
    #         7     9
    #        / \   / \
    #       6   5 2   3
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)

    sum = 12
    got = count_paths(root, sum)
    expected =  3
    # 7 -> 5
    # 1 -> 9 -> 2
    # 9 -> 3
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

    sum = 11
    got = count_paths(root, sum)
    # 7 -> 4
    # 1 -> 10
    expected = 2
    assert got == expected

def test_example_3():
    # Build this tree:
    #            1
    #          /   \
    #         7     9
    #        / \   / \
    #       6   5 2   3
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)

    sum = 12
    got = optimized_count_paths(root, sum)
    expected =  3
    # 7 -> 5
    # 1 -> 9 -> 2
    # 9 -> 3
    assert got == expected

def test_example_4():
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

    sum = 11
    got = optimized_count_paths(root, sum)
    # 7 -> 4
    # 1 -> 10
    expected = 2
    assert got == expected

