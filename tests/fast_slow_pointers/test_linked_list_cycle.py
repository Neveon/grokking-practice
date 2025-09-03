import pytest
from patterns.fast_slow_pointers.linked_list_cycle import linked_list_cycle, find_length_of_cycle
from tests.utils.linked_list_utils import build_linked_list

@pytest.fixture
def six_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5, 6])

def test_example_1(six_node_list):
    # pytest runs:
    #   value = six_node_list()   <-- behind the scenes
    #   test_example(value)
    head, _ = six_node_list
    got = linked_list_cycle(head)
    expected = False
    assert expected == got

def test_example_2(six_node_list):
    head, nodes = six_node_list
    # last node (6) points to node 3 → cycle
    nodes[-1].next = nodes[2]
    got = linked_list_cycle(head)
    expected = True
    assert expected == got

def test_cycle_length_1(six_node_list):
    head, nodes = six_node_list
    # last node (6) points to node 3 → cycle
    nodes[-1].next = nodes[2]
    got = find_length_of_cycle(head)
    expected = 4
    assert expected == got
