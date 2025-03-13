print("\n.........................Removing an element at the given position of DLL.........................\n")

class _Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def addlast(self, element):
        newest = _Node(element, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1
    
    def removeany(self, position):
        if self.isempty():
            print("List is empyt")
            return
        index = 1
        p = self._head
        while index < position - 1:
            p = p._next
            index = index + 1
        ele = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -= 1
        return ele
    
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        while p:
            print(p._element, end=' <-> ')
            p = p._next
        print("None")

    def display_reverse(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._tail
        while p:
            print(p._element, end=' <-> ')
            p = p._prev
        print("None")


DLL = DoubleLinkedList()
DLL.addlast(1)
DLL.addlast(2)
DLL.addlast(3)
DLL.addlast(4)
DLL.display()
print("After adding four element to the DLL, the size is:", len(DLL))
print()

ele = DLL.removeany(3)
DLL.display()
print("The deleted element:", ele)
print("After deleting an element at position 3, size is:", len(DLL))
print()

print("Printing DLL in reverse order:")
DLL.display_reverse()
