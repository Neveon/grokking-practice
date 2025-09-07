import pytest
from patterns.in_place_reversal_of_a_linked_list.reverse_every_k_element_sublist import reverse_every_k_element_sublist
from tests.utils.linked_list_utils import build_linked_list, linked_list_to_values


@pytest.fixture
def eight_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5, 6, 7, 8])

def test_reverse_eight_nodes_k_3(eight_node_list):
    head, _ = eight_node_list
    k = 3
    got_head = reverse_every_k_element_sublist(head, k)
    got_values = linked_list_to_values(got_head)
    expected_values = [3, 2, 1, 6, 5, 4, 8, 7]

    assert got_values == expected_values

def test_reverse_eight_nodes_k_6(eight_node_list):
    head, _ = eight_node_list
    k = 6
    got_head = reverse_every_k_element_sublist(head, k)
    got_values = linked_list_to_values(got_head)
    expected_values = [6, 5, 4, 3, 2, 1, 8, 7]

    assert got_values == expected_values

