print("\n.........................Inserting an element at the beginning of a Circular Doubly Linked List.........................\n")

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
        self._size = self._size + 1 

    
    def addfirst(self, element):
        newest = _Node(element)
        if self.isempty():
            self._head = newest
            self._head._prev = newest
            self._head._next = newest
        else:
            self._head._prev._next = newest
            newest._next = self._head
            newest._prev = self._head._prev
            self._head._prev = newest
            self._head = newest
        self._size += 1

    def display(self):
        if self.isempty():
            print("Circular Doubly Linked List is empty")
            return
        p = self._head
        print("Printing the elements of CDLL: ", end="")
        while p is not None:
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

CDLL.addfirst(3)
CDLL.addfirst(4)
CDLL.display()
print("After inserting two elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addlast(5)
CDLL.addfirst(6)
CDLL.display()
print("After inserting two elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addlast(7)
CDLL.display()
print("After inserting one more element at the end the size of the CDLL is:", len(CDLL))