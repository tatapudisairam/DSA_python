print("\n.........................Inserting an element at the end of a Singly-Linked list.........................\n")

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
        return self._size==0
    
    # for inserting an element at the end of the single linked list
    def addend(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size = self._size + 1

    # for displaying the entire single linked list
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        print("The linked list is:", end=" ")
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
L.addend(5)
L.display()
print("After adding one more element the size is:", len(L))