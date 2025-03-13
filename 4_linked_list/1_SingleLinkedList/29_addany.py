print("\n.........................Inserting an element at given position in the Linked list.........................\n")

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
        else:
            self._tail._next = newest
        self._tail = newest
        self._size = self._size + 1
    
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        print("Printint the elements of the linked list: ")
        while p:
            print(p._element, end=" -> ")
            p = p._next
        print("None")
    
    def addany(self, element, position):
        newest = _Node(element, None)
        p = self._head
        i = 1
        while i<=position-2:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

L = LinkedList()
L.addlast(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.display()
print("After adding four elements the size is   :", len(L))
print()
L.addany(5, 3)
L.display()
print("After adding 5 at the 3rd position the size is:", len(L))
