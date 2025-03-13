print("\n.........................Deleting an element at the end of the Linked list.........................\n")

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
    
    def isempty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
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

    def removelast(self):
        if self.isempty():
            print("Linked list is empty")
            return
        elif len(self)==1:
            e = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            return e
        p = self._head
        while p._next._next:
            p = p._next
        ele = p._next._element
        self._tail = p
        p = p._next
        self._tail._next = None
        self._size -= 1
        return ele

L = LinkedList()
L.addlast(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.display()
print("After adding four elements the size is   :", len(L))
print()
ele = L.removelast()
L.display()
print("The removed element is:", ele)
print("After deleting the last element size is:", len(L))
print()
ele = L.removelast()
L.display()
print("The removed element is:", ele)
print("After deleting the last element size is:", len(L))