print("\n.........................Searching for a element in Singly-Linked list.........................\n")

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
    
    def addend(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            else:
                p = p._next
                index = index+1
        return -1
    
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        print("Printing the elements of the linked list: ", end="")
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
n = eval(input("Enter the value to find the position in the above linked list: "))
result = L.search(n)
if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)