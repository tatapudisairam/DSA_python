print("\n.........................Inserting an element at the end of a Circular Doubly Linked List.........................\n")

class _Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, element, next=None, prev=None):
        self._element = element  
        self._next = next       
        self._prev = prev      

class CircularDoublyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def addlast(self, element):
        newest = _Node(element)
        if self.isempty():
            self._head = newest
            self._head._next = self._head  
            self._head._prev = self._head 
        else:
            tail = self._head._prev
            newest._prev = tail
            newest._next = self._head
            tail._next = newest
            self._head._prev = newest
        self._size += 1

    def display(self):
        if self.isempty():
            print("The Circular Doubly Linked List is empty.")
            return
        p = self._head
        print("Printing the elements of CDLL: ", end="")
        while p is not None:
            print(p._element, end=" <-> ")
            p = p._next
            if p == self._head:  
                break
        print("Back to head")

CDLL = CircularDoublyLinkedList()
CDLL.addlast(1)
CDLL.addlast(2)
CDLL.addlast(3)
CDLL.addlast(4)
CDLL.display()
print("After inserting four elements the size of the CDLL is:", len(CDLL))
print()

CDLL.addlast(5)
CDLL.display()
print("After inserting one more element at the end the size of the CDLL is:", len(CDLL))
