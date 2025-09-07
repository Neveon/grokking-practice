import pytest
from patterns.in_place_reversal_of_a_linked_list.reverse_sub_list import reverse_sub_list
from tests.utils.linked_list_utils import build_linked_list


@pytest.fixture
def six_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5])


def linked_list_to_values(head):
    """Helper: walk the linked list and return all values as a list."""
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values


def test_reverse_six_nodes(six_node_list):
    head, _ = six_node_list
    p, q = 2, 4
    got_head = reverse_sub_list(head, p, q)
    got_values = linked_list_to_values(got_head)
    expected_values = [1, 4, 3, 2, 5]

    assert got_values == expected_values

def test_reverse_all_nodes(six_node_list):
    head, _ = six_node_list
    p, q = 1, 5
    got_head = reverse_sub_list(head, p, q)
    got_values = linked_list_to_values(got_head)
    expected_values = [5, 4, 3, 2, 1]

    assert got_values == expected_values
