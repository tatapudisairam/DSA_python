print("\n.........................Searching for an element in Circlar Linked list.........................\n")


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
    
    def addlast(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def search(self, key):
        if self.isempty():
            print("List is empty")
            return -1
        p = self._head
        index = 0
        while True:
            if p._element == key:
                return index
            else:
                p = p._next
                index = index+1
            if p == self._head:
                break
        return -1
    
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

L = LinkedList()
L.addlast(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.display()
print("After adding four elements the size is   :", len(L))
n = eval(input("Enter the value to find the position in the above linked list: "))
result = L.search(n)
if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)