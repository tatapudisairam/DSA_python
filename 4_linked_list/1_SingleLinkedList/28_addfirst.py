print("\n.........................Inserting an element at the beginning of the Linked list.........................\n")

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
    
    def addend(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addfirst(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
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

    
L = LinkedList()
L.addend(1)
L.addend(2)
L.addend(3)
L.addend(4)
L.display()
print("After adding four elements the size is   :", len(L))
print()
L.addfirst(5)
L.display()
print("After adding one element at the beginning the size is   :", len(L))