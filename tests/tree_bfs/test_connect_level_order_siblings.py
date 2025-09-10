import pytest
from patterns.tree_bfs.connect_level_order_siblings import connect_level_order_siblings, grokking_solution
from tests.utils.tree import TreeNode


def collect_levels_by_next(root: TreeNode):
    """
    Traverse the tree level by level using the 'next' pointers.
    Returns a list of lists with node values per level.
    """
    levels = []
    level_start = root

    while level_start:
        curr = level_start
        line = []
        next_level_start = None

        # Walk the current level using .next
        while curr:
            line.append(curr.value)
            # Determine the first node of the next level (leftmost child)
            if next_level_start is None:
                next_level_start = curr.left or curr.right
            curr = curr.next

        levels.append(line)
        level_start = next_level_start

    return levels


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

    # Connect siblings
    connect_level_order_siblings(root)

    # Expected next chains:
    # 1 -> None
    # 2 -> 3 -> None
    # 4 -> 5 -> 6 -> 7 -> None
    expected_levels = [[1], [2, 3], [4, 5, 6, 7]]
    assert collect_levels_by_next(root) == expected_levels

    # Spot-check some explicit .next pointers as well:
    assert root.next is None
    assert root.left.next is root.right
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.left
    assert root.right.left.next is root.right.right
    assert root.right.right.next is None


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

    # Connect siblings
    connect_level_order_siblings(root)

    # Expected next chains:
    # 1 -> None
    # 2 -> 3 -> None
    # 4 -> 5 -> 6 -> None
    expected_levels = [[1], [2, 3], [4, 5, 6]]
    assert collect_levels_by_next(root) == expected_levels

    # Spot-check .next pointers:
    assert root.next is None
    assert root.left.next is root.right
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.left
    assert root.right.left.next is None

def test_grokking_example_1():
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

    # Connect siblings
    grokking_solution(root)

    # Expected next chains:
    # 1 -> None
    # 2 -> 3 -> None
    # 4 -> 5 -> 6 -> 7 -> None

    assert root.next is None
    assert root.left.next is root.right
    assert root.right.next is None
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.left
    assert root.right.left.next is root.right.right
    assert root.right.right.next is None


def test_grokking_example_2():
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

    # Connect siblings
    grokking_solution(root)

    # Expected next chains:
    # 1 -> None
    # 2 -> 3 -> None
    # 4 -> 5 -> 6 -> None

    assert root.next is None
    assert root.left.next is root.right
    assert root.right.next is None
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.left
    assert root.right.left.next is None
