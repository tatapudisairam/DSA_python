print("\n.........................Removing an element at given position in the Linked list.........................\n")

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def addlast(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1
    
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        print("Printing the elements of the linked list: ")
        while p:
            print(p._element, end=" -> ")
            p = p._next
        print("None")
    
    def removeany(self, position):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i = i+1
        ele = p._next._element
        p._next = p._next._next
        self._size -= 1
        return ele

L = LinkedList()
L.addlast(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.addlast(5)
L.addlast(6)
L.addlast(7)
L.display()
print("After adding seven elements the size is   :", len(L))
print()
ele = L.removeany(4)
L.display()
print("The removed element is:", ele)
print("After deleting 4th element size is:", len(L))
print()
ele = L.removeany(3)
L.display()
print("The removed element is:", ele)
print("After deleting 3rd element size is:", len(L))
