print("\n.........................Linear Probing - Collision Detection scheme.........................\n")

class HashLinearProbe:
    def __init__(self, size):
        self._hashTableSize = size
        self._hashTable = [0] * self._hashTableSize
    
    def hashcode(self, key):
        return key % self._hashTableSize
    
    def lprobe(self, key):
        i = self.hashcode(key)
        j = 0
        while self._hashTable[(i+j) % self._hashTableSize] != 0:
            j = j+1
        return (i+j) % self._hashTableSize
    
    def insert(self, element):
        i = self.hashcode(element)
        if self._hashTable[i] == 0:
            self._hashTable[i] = element
        else:
            i = self.lprobe(element)
            self._hashTable[i] = element
    
    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self._hashTable[(i+j) % self._hashTableSize] != 0:
            if self._hashTable[(i+j) % self._hashTableSize] == key:
                return True
            j = j+1
            if j == self._hashTableSize:
                break
        return False

    def display(self):
        print(self._hashTable)

H = HashLinearProbe(12)
L = [78, 64, 92, 34, 86, 28]
for i in L:
    H.insert(i)
H.display()
print("Search 64:", H.search(64))
print("Serach 63:", H.search(63))