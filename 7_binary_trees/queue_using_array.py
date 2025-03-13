class QueuesArray:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data)==0
    
    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._data.pop(0)
    
    def front(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._data[0]
    
    def display(self):
        if self.isempty():
            print("Queue is emptpy")
            return
        print("The queue is: ", end="")
        for i in self._data:
            print(i, end=" ")
        print()
    
def main():
    q = QueuesArray()

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