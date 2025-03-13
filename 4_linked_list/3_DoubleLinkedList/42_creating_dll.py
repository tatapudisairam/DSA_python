print("\n.........................Creating nodes for DLL.........................\n")

class _Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, element, next, prev):
        self._element = element
        self._next = None
        self._prev = None

n1 = _Node(1, None, None)
n2 = _Node(2, None, None)
n1._next = n2
n2._prev = n1
print("Element of the n1:", n1._element)
print("Element of the n2:", n1._next._element)
print("Element of the n1:", n2._prev._element)