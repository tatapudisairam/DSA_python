class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next=None):
        self._element = element
        self._next = next

class QueuesLinkedList:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def enqueue(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        else:
            self._rear._next = newest
            self._rear = newest
        self._size += 1
    
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        elif len(self)==1:
            ele = self._front._element
            self._front = None
            self._rear = None
            self._size -= 1
            return ele
        ele = self._front._element
        self._front = self._front._next
        self._size -= 1
        return ele
    
    def front(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._front._element
    
    def display(self):
        if self.isempty():
            print("Queue is empty")
            return
        p = self._front
        print("Front", end="-> ")
        while p:
            print(p._element, end=' <- ')
            p = p._next
        print("Rear")
