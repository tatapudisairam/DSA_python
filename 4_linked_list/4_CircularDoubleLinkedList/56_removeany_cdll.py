print("\n.........................Removing an element at the given position of a Circular Doubly Linked List.........................\n")

class _Node:
    __slots__ = "_element", "_next", "_prev"
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

    def removeany(self, position):
        if self.isempty():
            print("Circular Double Linked list is empty")
            return
        index = 1
        temp = self._head
        while index < position-1:
            temp = temp._next
            index = index+1
        ele = temp._next._element
        temp._next._next._prev = temp
        temp._next = temp._next._next
        self._size -= 1
        return ele

    
    def display(self):
        if self.isempty():
            print("Circular Double Linked list is empty")
            return
        p = self._head
        print("Printing the elements of the CDLL : ", end="")
        while p:
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

CDLL.addlast(3)
CDLL.addlast(4)
CDLL.display()
print("After inserting two elements the size of the CDLL is:", len(CDLL))
print()

ele = CDLL.removeany(3)
print("The removed element", ele)
ele = CDLL.removeany(2)
print("The removed element", ele)
CDLL.display()
print("After removing two elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addlast(7)
CDLL.display()
print("After inserting one element the size of the CDLL is:", len(CDLL))
print()
