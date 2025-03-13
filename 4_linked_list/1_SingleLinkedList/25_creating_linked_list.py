print("\n.........................Creating nodes and Linked List.........................\n")

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

    
node_1 = _Node(4, None)
node_2 = _Node(5, None)
node_1._next = node_2
print("Element of the node_1:", node_1._element)
print("Link field of the node_1:", node_1._next)
print("Element of the node_2:", node_1._next._element)
