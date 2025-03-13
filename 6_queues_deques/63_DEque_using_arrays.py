print("\n.........................Implementation of Double Ended Queues using Arrays.........................\n")

class DEQuesArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data) == 0
    
    def addlast(self, element):
        self._data.append(element)
    
    def addfirst(self, element):
        self._data.insert(0, element)

    def removelast(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data.pop()
    
    def removefirst(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data.pop(0)
    
    def first(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data[0]
    
    def last(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data[-1]
    

def main():
    DQ = DEQuesArray()
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
            DQ.addfirst(ele)
            print("Added")
        elif n == 2:
            ele = input("Enter the element: ")
            if ele.isdigit() or ele.replace(".", "").isdigit():
                ele = eval(ele)
            DQ.addlast(ele)
            print("Added")
        elif n == 3:
            print("Removed element at the front is:", DQ.removefirst())
        elif n == 4:
            print("Removed element at the rear is:", DQ.removelast())
        elif n == 5:
            print("Front element of the queue:", DQ.first())
        elif n == 6:
            print("Rear element of the queue:", DQ.last())
        elif n == 7:
            print("The DEQue is:", DQ._data)
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