class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def build_linked_list(values: list[int]) -> tuple[Node, list[Node]]:
    """
    Builds a linked list from a list of values.
    Returns (head, nodes) where nodes is a list of Node objects.
    """

    head = Node(values[0])
    nodes = [head]
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
        nodes.append(current)

    return head, nodes

def linked_list_to_values(head):
    """Helper: walk the linked list and return all values as a list."""
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values

