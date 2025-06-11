print("\n.........................Inserting element into the Heap DS (Max-heap).........................\n")

class Heap:
    def __init__(self, size):
        self._maxsize = size
        self._current_size = 0
        self._data = [None]*self._maxsize
    
    def __len__(self):
        return self._current_size
    
    def isempty(self):
        return self._current_size == 0
    
    # for 1-based indexing
    # def insert(self, e):
    #     if self._current_size == self._maxsize:
    #         print("No space in the Heap")
    #         return
    #     self._current_size += 1
    #     hi = self._current_size
    #     while hi > 1 and e > self._data[hi//2]:
    #         self._data[hi] = self._data[hi//2]
    #         hi = hi//2
    #     self._data[hi] = e


    # for 0-based indexing
    def insert(self, e):
        if self._current_size == self._maxsize:
            print("No space in the Heap")
            return
        hi = self._current_size
        self._current_size += 1
        while hi > 0 and  e > self._data[(hi-1)//2]:
            self._data[hi] = self._data[(hi-1)//2]
            hi = (hi-1)//2
        self._data[hi] = e

    def max(self):
        if self._current_size == 0:
            print("Heap is empty")
            return
        # return self._data[1] # for 1-based indexing
        return self._data[0] # for 0-based indexing
    
H = Heap(10)
H.insert(25)
L = [14, 2, 20, 10, 40]
for i in L:
    H.insert(i)
print("After inserting 6 elements into the Heap :", H._data)
# print("After inserting 6 elements into the Heap :", H._data[:H._current_size+1]) # for 1-based indexing
print("After inserting 6 elements into the Heap :", H._data[:H._current_size]) # for 0-based indexing
print("Maximum element of the Heap :", H.max())