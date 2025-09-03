import pytest
from patterns.fast_slow_pointers.start_of_linked_list import start_of_linked_list
from tests.utils.linked_list_utils import build_linked_list

@pytest.fixture
def six_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5, 6])

def test_example_1(six_node_list):
    head, nodes = six_node_list
    # last node (6) points to node 4
    # node 4 is start of cycle
    nodes[-1].next = nodes[3]
    got = start_of_linked_list(head)
    expected = nodes[3]
    assert expected == got

def test_example_2(six_node_list):
    head, nodes = six_node_list
    # last node (6) points to node 1
    nodes[-1].next = nodes[0]
    got = start_of_linked_list(head)
    expected = nodes[0]
    assert expected == got
