print("\n.........................Chaining - Collision Detection scheme.........................\n")
class _Node:
    __slots__ = "_element", "_next"
    def __init__(self, ele):
        self._element = ele
        self._next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def insertSorted(self, e):
        newest = _Node(e)
        if self.isempty():
            self._head = newest
        else:
            p = self._head
            q = self._head
            while p and p._element < e:
                q = p
                p = p._next
            if p == self._head:
                newest._next = self._head
                self._head = newest
            else:
                newest._next = q._next
                q._next = newest
        self._size += 1

    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        while p:
            print(p._element, end=" -> ")
            p = p._next
        print("None")

    def search(self, key):
        if self.isempty():
            return False
        p = self._head
        while p:
            if p._element == key:
                return True
            else:
                p = p._next
        return False

class HashChaining:
    def __init__(self, size):
        self.hashTableSize = size
        self.hashTable = [-1] * self.hashTableSize
        for i in range(self.hashTableSize):
            self.hashTable[i] = LinkedList()

    def hashcode(self, key):
        return key % self.hashTableSize
    
    def insert(self, e):
        i = self.hashcode(e)
        self.hashTable[i].insertSorted(e)

    def display(self):
        for i in range(self.hashTableSize):
            print('[', i, '] ', sep="", end="")
            self.hashTable[i].display()
        print()

    def search(self, key):
        i = self.hashcode(key)
        if self.hashTable[i].search(key):
            print(key, "is found")
        else:
            print(key, "is not found")


SIZE = 10
H = HashChaining(SIZE)
L = [54, 78, 64, 92]
for i in L:
    H.insert(i)
H.display()
H.insert(34)
H.insert(28)
H.display()
H.search(54)
H.search(55)