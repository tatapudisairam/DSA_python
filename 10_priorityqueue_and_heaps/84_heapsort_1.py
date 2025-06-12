print("\n.........................Heap Sort without heapify.........................\n")

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
        if self._csize == self._maxsize:
            print("No space is the Heap")
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
        while j < self._csize:
            if j+1 < self._csize and self._data[j] < self._data[j+1]:
                j = j+1
            if self._data[j] > self._data[i]:
                self._data[i], self._data[j] = self._data[j], self._data[i]
                i = j
                j = 2*i+1
            else:
                break
        return e
    
def heap_sort(arr):
    H = Heap(len(arr))
    for i in range(len(arr)):
        H.insert(arr[i])
    
    for i in range(len(arr)-1, -1, -1):
        arr[i] = H.deleteMax()


inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
heap_sort(l1)
print("Sorted list: ", l1)