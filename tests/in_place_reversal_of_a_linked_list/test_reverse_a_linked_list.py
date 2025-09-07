import pytest
from patterns.in_place_reversal_of_a_linked_list.reverse_a_linked_list import reverse_linked_list
from tests.utils.linked_list_utils import build_linked_list


@pytest.fixture
def six_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 4, 6, 8, 10])


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
    got_head = reverse_linked_list(head)

    # Verify reversed order
    got_values = linked_list_to_values(got_head)
    expected_values = [10, 8, 6, 4, 2, 1]

    assert got_values == expected_values


def test_reverse_single_node():
    head, _ = build_linked_list([42])
    got_head = reverse_linked_list(head)
    assert linked_list_to_values(got_head) == [42]

