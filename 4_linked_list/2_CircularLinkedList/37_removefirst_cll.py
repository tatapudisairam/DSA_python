print("\n.........................Deleting an element at the beginning of the Circular Linked list.........................\n")

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class CircularLinkedList:
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
            newest._next = newest
        else:
            newest._next = self._head
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print("List is empty")
            return
        ele = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None
        return ele
    
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        while True:
            print(p._element, end=" --> ")
            p = p._next
            if p == self._head:
                break
        print("Back to head")


CLL = CircularLinkedList()
CLL.addlast(1)
CLL.addlast(2)
CLL.addlast(3)
CLL.addlast(4)
CLL.display()
print("After inserting four elements the size of the CLL is:", len(CLL))
print()

ele = CLL.removefirst()
CLL.display()
print("The removed element is:", ele)
print("After deleting an element at the beginning, the size is:", len(CLL))