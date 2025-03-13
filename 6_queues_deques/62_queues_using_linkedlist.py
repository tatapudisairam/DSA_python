print("\n.........................Implementation of Queues using LinkedList.........................\n")

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
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

def main():
    q = QueuesLinkedList()
    while True:
        print("\nChoose an option:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. front of the queue")
        print("4. Display the queue")
        print("5. length of the queue")
        print("6. isEmpty ?")
        print("7. Exit") 

        n = int(input("Enter the choice: "))

        if n == 1:
            ele = input("Enter the element: ")
            if ele.isdigit() or ele.replace(".", "").isdigit():
                ele = eval(ele)
            q.enqueue(ele)
            print("Added")
        elif n == 2:
            print("Removed element at the front is:", q.dequeue())
        elif n == 3:
            print("Front element of the queue:", q.front())
        elif n == 4:
            q.display()
        elif n == 5:
            print("The length of the queue:", len(q))
        elif n == 6:
            print(q.isempty())
        elif n == 7:
            print("Exiting....")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == '__main__':
    main()