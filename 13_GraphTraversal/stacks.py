class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class StacksLinkedList:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
    
    def pop(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        ele = self._top._element
        self._top = self._top._next
        self._size -= 1
        return ele

    def peek(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        return self._top._element
    
    def traverse(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        p = self._top
        print("top", end="")
        while p:
            print(f' -> {p._element}', end="")
            p = p._next
