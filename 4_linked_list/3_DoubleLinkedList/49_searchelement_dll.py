print("\n.........................Searching for an element in Double Linked list.........................\n")

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
    
    def search(self, key):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            else:
                p = p._next
                index = index + 1

        return -1

    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        while p:
            print(p._element, end=' <-> ')
            p = p._next
        print("None")

DLL = DoubleLinkedList()
DLL.addlast(1)
DLL.addlast(2)
DLL.addlast(3)
DLL.addlast(4)
DLL.display()
print("After adding four elements the size is   :", len(DLL))
n = eval(input("Enter the value to find the position in the above linked list: "))
result = DLL.search(n)
if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)

