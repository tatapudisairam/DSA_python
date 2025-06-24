print("\n.........................Double Hashing - Collision Detection scheme.........................\n")

class HashDoubleHashing:
    def __init__(self, size):
        self._hashTableSize = size
        self._hashTable = [None] * self._hashTableSize
        self._prime = self._find_largest_prime_less_than(size)

    def _is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def _find_largest_prime_less_than(self, n):
        for i in range(n - 1, 1, -1):
            if self._is_prime(i):
                return i
        return 1

    def hash1(self, key):
        return key % self._hashTableSize
    
    def hash2(self, key):
        return self._prime - (key%self._prime)
    
    def insert(self, element):
        i = self.hash1(element)
        j = self.hash2(element)
        for k in range(self._hashTableSize):
            index = (i + k * j) % self._hashTableSize
            if self._hashTable[index] is None:
                self._hashTable[index] = element
                return
        print(f"Table Full: Couldn't insert {element}")

    def search(self, key):
        i = self.hash1(key)
        j = self.hash2(key)
        for k in range(self._hashTableSize):
            index = (i + k * j) % self._hashTableSize
            if self._hashTable[index] is None:
                return False
            if self._hashTable[index] == key:
                return True
        return False
    
    def display(self):
        print(self._hashTable)

H = HashDoubleHashing(15)
L = [18, 41, 22, 44, 59, 32, 31]
for i in L:
    H.insert(i)
H.display()
print("Search 44:", H.search(44))  
print("Search 99:", H.search(99))  