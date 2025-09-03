import pytest
from patterns.fast_slow_pointers.middle_of_the_linked_list import middle_of_linked_list, middle_of_linked_list_fast_slow
from tests.utils.linked_list_utils import build_linked_list

@pytest.fixture
def five_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5])

@pytest.fixture
def six_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5, 6])

@pytest.fixture
def seven_node_list():
    # Fresh list for every test
    return build_linked_list([1, 2, 3, 4, 5, 6, 7])

def test_example_1(five_node_list):
    head, nodes = five_node_list
    got = middle_of_linked_list(head)
    expected = 3
    assert expected == got

def test_example_2(six_node_list):
    head, nodes = six_node_list
    got = middle_of_linked_list(head)
    expected = 4
    assert expected == got

def test_example_3(seven_node_list):
    head, nodes = seven_node_list
    got = middle_of_linked_list(head)
    expected = 4
    assert expected == got

def fast_slow_test_1(five_node_list):
    head, nodes = five_node_list
    got = middle_of_linked_list_fast_slow(head)
    expected = 3
    assert expected == got

def fast_slow_test_2(six_node_list):
    head, nodes = six_node_list
    got = middle_of_linked_list_fast_slow(head)
    expected = 4
    assert expected == got

def fast_slow_test_3(seven_node_list):
    head, nodes = seven_node_list
    got = middle_of_linked_list_fast_slow(head)
    expected = 4
    assert expected == got
