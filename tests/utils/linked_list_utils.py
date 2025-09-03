class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def build_linked_list(values):
    """
    Builds a linked list from a list of values.
    Returns (head, nodes) where nodes is a list of Node objects.
    """
    if not values:
        return None, []

    head = Node(values[0])
    nodes = [head]
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
        nodes.append(current)

    return head, nodes
