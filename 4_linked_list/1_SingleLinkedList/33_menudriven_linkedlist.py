print("\n.........................Menu Driven program of the Single Linked list.........................\n")

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
    
    def addlast(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        print("Added")
    
    def addfirst(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1
        print("Added")
    
    def addany(self, element, position):
        newest = _Node(element, None)
        if position == self._size+1:
            self.addlast(element)
            return
        elif position == 1:
            self.addfirst(element)
            return
        p = self._head
        index = 1
        while index < position-1:
            p = p._next
            index = index+1
        newest._next = p._next
        p._next = newest
        self._size += 1
        print("Added")
    
    def removelast(self):
        if self.isempty():
            print("Linked list is empty")
            return
        elif len(self)==1:
            e = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            print("The deleted element at the end is: ", e)
            return
        p = self._head
        while p._next._next:
            p = p._next
        ele = p._next._element
        self._tail = p
        p = p._next
        self._tail._next = None
        self._size -= 1
        print("The deleted element at the end is: ", ele)

    def removefirst(self):
        if self.isempty():
            print("Linked list is empty")
            return
        p = self._head
        self._head = p._next
        ele = p._element
        p._next = None
        self._size -= 1
        print("The deleted element at beginning is: ", ele)

    def removeany(self, position):
        if self.isempty():
            print("Linked list is empty")
            return
        if position == self._size:
            self.removelast()
            return
        elif position == 1:
            self.removefirst()
            return
        p = self._head
        index = 1
        while index < position-1:
            p = p._next
            index += 1
        ele = p._next._element
        p._next = p._next._next
        self._size -= 1
        print("The deleted element at position", position, "is: ", ele)
    
    def search(self, key):
        if self.isempty():
            print("Linked list is empty")
            return
        p = self._head
        index = 1
        while p:
            if p._element == key:
                print("The element is found at position: ", index)
                return
            p = p._next
            index += 1
        print("Element not found in the Linked list")
    
    def display(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        print("Linked list is: ")
        while p:
            print(p._element, end=" -> ")
            p = p._next
        print("None")
        


def main():
    l = LinkedList()
    while True:
        print("\nChoose an option:")
        print("1. Add element at the end")
        print("2. Add element at the beginning")
        print("3. Add element at a specific position")
        print("4. Remove an element from the end")
        print("5. Remove an element from the beginning")
        print("6. Remove an element from the a specific position")
        print("7. Display the linked list")
        print("8. Search for an element")
        print("9. Size of the linked list")
        print("10. Exit")

        n = int(input("Enter your choice: "))
        if n == 1:
            element = eval(input("Enter the element: "))
            l.addlast(element)
        elif n == 2:
            element = eval(input("Enter the element: "))
            l.addfirst(element)
        elif n == 3:
            element = eval(input("Enter the element: "))
            position = int(input("Enter the position: "))
            if position >0 and position <= len(l)+1:
                l.addany(element, position) 
            else:
                print("Invalid position")
        elif n == 4:
            l.removelast()
        elif n == 5:
            l.removefirst()
        elif n == 6:
            position = int(input("Enter the position: "))
            if position >0 and position < len(l)+1:
                l.removeany(position)
            else:
                print("Invalid position")
        elif n == 7:
            l.display()
        elif n == 8:
            element = eval(input("Enter the element: "))
            l.search(element)
        elif n == 9:
            print("The size is:", len(l))
        elif n == 10:
            print("Exiting....")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()