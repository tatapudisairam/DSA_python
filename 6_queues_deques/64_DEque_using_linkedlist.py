print("\n.........................Implementation of Double Ended Queues using Linked list.........................\n")

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class DEQueLinkedList:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def enqueuelast(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        else:
            self._rear._next = newest
            self._rear = newest
        self._size += 1

    def enqueuefirst(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1
    
    def dequeuefirst(self):
        if self.isempty():
            print("DEQue is empty")
            return
        elif len(self)==1:
            ele = self._rear._element
            self._rear = None
            self._front = None
            self._size -= 1
            return ele
        ele = self._front._element
        self._front = self._front._next
        self._size -= 1
        return ele

    def dequeuelast(self):
        if self.isempty():
            print("DEQue is empty")
            return
        elif len(self)==1:
            ele = self._rear._element
            self._rear = None
            self._front = None
            self._size -= 1
            return ele
        ele = self._rear._element
        p = self._front
        while p._next._next:
            p = p._next
        self._rear = p
        p = p._next
        self._rear._next = None
        self._size -= 1
        return ele
    
    def first(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._front._element
    
    def last(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._rear._element
    
    def display(self):
        p = self._front
        while p:
            print(p._element, end=' -> ')
            p = p._next
        print("None")


def main():
    DQ = DEQueLinkedList()
    while True:
        print("\nChoose an option:")
        print("1. Enqueue an element at front")
        print("2. Enqueue an element at rear")
        print("3. Dequeue an element at front")
        print("4. Dequeue an element at rear")
        print("5. front of the queue")
        print("6. rear of the queue")
        print("7. Display the queue")
        print("8. length of the queue")
        print("9. isEmpty ?")
        print("10. Exit") 

        n = int(input("Enter the choice: "))

        if n == 1:
            ele = input("Enter the element: ")
            if ele.isdigit() or ele.replace(".", "").isdigit():
                ele = eval(ele)
            DQ.enqueuefirst(ele)
            print("Added")
        elif n == 2:
            ele = input("Enter the element: ")
            if ele.isdigit() or ele.replace(".", "").isdigit():
                ele = eval(ele)
            DQ.enqueuelast(ele)
            print("Added")
        elif n == 3:
            print("Removed element at the front is:", DQ.dequeuefirst())
        elif n == 4:
            print("Removed element at the rear is:", DQ.dequeuelast())
        elif n == 5:
            print("Front element of the queue:", DQ.first())
        elif n == 6:
            print("Rear element of the queue:", DQ.last())
        elif n == 7:
            print("The DEQue is:")
            DQ.display()
        elif n == 8:
            print("The length of the Double Ended queue:", len(DQ))
        elif n == 9:
            print(DQ.isempty())
        elif n == 10:
            print("Exiting....")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == '__main__':
    main()