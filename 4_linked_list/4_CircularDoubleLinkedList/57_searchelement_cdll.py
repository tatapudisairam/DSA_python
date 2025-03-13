print("\n.........................Searching for an element in Circular Double Linked list.........................\n")

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
    
    def search(self, key):
        if self.isempty():
            print("Circular Double Linked list is empty")
            return
        p = self._head
        pos = 1
        while p:
            if p._element == key:
                print("The element", key,"is found at postion : ", pos)
                return
            p = p._next
            pos = pos + 1
            if p == self._head:
                break
        print("Element",key,"not found")

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

CDLL.search(3)
CDLL.display()
print()

CDLL.addlast(7)
CDLL.search(7)
CDLL.display()
print()

CDLL.search(10)
CDLL.display()
print()
