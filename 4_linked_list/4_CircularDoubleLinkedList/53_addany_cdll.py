print("\n.........................Inserting an element at the given position of a Circular Doubly Linked List.........................\n")

class _Node:
    __slots__ = "_element", "_prev", "_next"
    def __init__(self, element):
        self._element = element
        self._prev = None
        self._next = None
    
class CircularDoubleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, element):
        newest = _Node(element)
        if self.isempty():
            self._head = newest
            self._head._prev = newest
            self._head._next = newest
        else:
            newest._prev = self._head._prev
            self._head._prev._next = newest
            self._head._prev = newest
            newest._next = self._head
        self._size += 1

    def addany(self, element, position):
        newest = _Node(element)
        index = 1
        p = self._head
        while index < position-1:
            p = p._next
            index += 1
        newest._next = p._next
        p._next = newest
        newest._next._prev = newest
        newest._prev = p
        self._size += 1

    def display(self):
        if self.isempty():
            print("Circular Double Linked List is empty")
            return
        p = self._head
        print("Printing the elements of CDLL : ", end="")
        while True:
            print(p._element, end=" <-> ")
            p = p._next
            if p == self._head:
                break
        print("Back to head")

CDLL = CircularDoubleLinkedList()
CDLL.addlast(1)
CDLL.addlast(2)
CDLL.display()
print("After inserting two elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addany(3, 2)
CDLL.addany(4, 3)
CDLL.display()
print("After inserting two elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addlast(5)
CDLL.addany(6, 3)
CDLL.display()
print("After inserting two elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addlast(7)
CDLL.display()
print("After inserting one more element at the end the size of the CDLL is:", len(CDLL))