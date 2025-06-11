print("\n.........................Removing element from the Heap DS (Max-heap).........................\n")

class Heap:
    def __init__(self, size):
        self._maxsize = size
        self._data = [None]*self._maxsize
        self._csize = 0
    
    def __len__(self):
        return self._csize
    
    def isempty(self):
        return self._csize == 0
    
    def insert(self, e):
        if self._maxsize == self._csize:
            print("No space in the Heap")
            return
        hi = self._csize
        self._csize += 1
        while hi > 0 and e > self._data[(hi-1)//2]:
            self._data[hi] = self._data[(hi-1)//2]
            hi = (hi-1)//2
        self._data[hi] = e

    def deleteMax(self):
        if self._csize == 0:
            print("Heap is empty")
            return
        e = self._data[0]
        self._data[0] = self._data[self._csize-1]
        self._data[self._csize-1] = None
        self._csize -= 1
        i = 0
        j = 2*i+1
        while j<self._csize:
            if j+1 < self._csize and self._data[j+1] > self._data[j]:
                j = j+1
            if self._data[i] < self._data[j]:
                self._data[i], self._data[j] = self._data[j], self._data[i]
                i = j
                j = 2*i + 1
            else:
                break
        return e
    
    # for 1-based indexing
    # def deletemax(self):
    #     if self._csize == 0:
    #         print('Heap is Empty')
    #         return
    #     e = self._data[1]
    #     self._data[1] = self._data[self._csize]
    #     self._data[self._csize] = -1
    #     self._csize = self._csize - 1
    #     i = 1
    #     j = i * 2
    #     while j <= self._csize:
    #         if self._data[j] < self._data[j+1]:
    #             j = j + 1
    #         if self._data[i] < self._data[j]:
    #             temp = self._data[i]
    #             self._data[i] = self._data[j]
    #             self._data[j] = temp
    #             i = j
    #             j = i * 2
    #         else:
    #             break
    #     return e

    def max(self):
        if self._csize == 0:
            print("Heap is empty")
            return
        return self._data[0]
    
H = Heap(10)
H.insert(30)
H.insert(40)
H.insert(25)
H.insert(15)
H.insert(50)

print("Heap array:", H._data)
print("Deleted max:", H.deleteMax())
print("Heap array after deletion:", H._data)
print("Maxmum of the Heap:", H.max())