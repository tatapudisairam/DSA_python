print("\n.........................Menu Driven program of the Circular Double Linked list.........................\n")

class _Node:
    __slots__ = "_element", "_prev", "_next"
    def __init__(self, element):
        self._element = element
        self._prev = None
        self._next = None

class CircularDoubleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def addlast(self, element):
        newest = _Node(element)
        if self.isempty():
            self._head = newest
            self._head._prev = newest
            self._head._next = newest
        else:
            newest._prev = self._head._prev
            self._head._prev._next = newest
            self._head._prev = newest
            newest._next = self._head
        self._size += 1
        print("Added")

    def addfirst(self, element):
        newest = _Node(element)
        if self.isempty():
            self._head = newest
            self._head._prev = newest
            self._head._next = newest
        else:
            newest._prev = self._head._prev
            newest._next = self._head
            self._head._prev._next = newest
            self._head._prev = newest
            self._head = newest
        self._size += 1
        print("Added")
    
    def addany(self, element, position):
        if position == 1:
            self.addfirst(element)
            return
        if position == self._size+1:
            self.addlast(element)
            return
        newest = _Node(element)
        p = self._head
        index = 1
        while index < position-1:
            p = p._next
            index += 1
        p._next._prev = newest
        newest._prev = p
        newest._next = p._next
        p._next = newest
        self._size += 1
        print("Added")
    
    def removefirst(self):
        if self.isempty():
            print("Circular Dobule Linked List is empty")
            return
        if self._size == 1:
            ele = self._head._element
            self._head = None
        else:
            ele = self._head._element
            self._head._prev._next = self._head._next
            self._head._next._prev = self._head._prev
            self._head = self._head._next
        self._size -= 1
        print("The deleted element at beginning is: ", ele)

    def removelast(self):
        if self.isempty():
            print("Circular Double Linked list is empty")
            return
        if self._size == 1:
            ele = self._head._element
            self._head = None
        else:
            ele = self._head._prev._element
            self._head._prev = self._head._prev._prev
            self._head._prev._next = self._head
        self._size -= 1
        print("The deleted element at end is: ", ele)

    def removeany(self, position):
        if position == 1:
            self.removefirst()
            return
        elif position == self._size:
            self.removelast()
            return
        index = 1
        p = self._head
        while index < position-1:
            p = p._next
            index += 1
        ele = p._next._element
        p._next._next._prev = p
        p._next = p._next._next
        self._size -= 1
        print("The deleted element at position", position, "is :", ele)
    
    def search(self, key):
        if self.isempty():
            print("Circular Double Linked list is empty")
            return
        p = self._head
        index = 1
        while p:
            if p._element == key:
                print("Element", key, "is found at position", index)
                return
            index += 1
            p = p._next
            if p == self._head:
                break
        print("Element", key, "not found")


    def display(self):
        if self.isempty():
            print("Circular Double Linked list is empty")
            return
        p = self._head
        print("Printing the elements of CDLL : ", end="")
        while p:
            print(p._element, end=" <-> ")
            p = p._next
            if p == self._head:
                break
        print("Back to head")


def main():
    CDLL = CircularDoubleLinkedList()
    while True:
        print("\nChoose an option:")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Insert at required position")
        print("4. Remove last")
        print("5. Remove first")
        print("6. Remove at required position")
        print("7. Search for an element")
        print("8. Display CDLL")
        print("9. Size of the CDLL")
        print("10. Quit")

        n = int(input("Enter your choice : "))
        if n == 1:
            element = eval(input("Enter the element : "))
            CDLL.addlast(element)
        elif n == 2:
            element = eval(input("Enter the element : "))
            CDLL.addfirst(element)
        elif n == 3:
            element = eval(input("Enter the element : "))
            position = int(input("Enter the position : "))
            if position > 0 and position <= len(CDLL)+1:
                CDLL.addany(element, position)
            else:
                print("Invalid position!")
        elif n == 4:
            CDLL.removelast()
        elif n == 5:
            CDLL.removefirst()
        elif n == 6:
            position = int(input("Enter the position : "))
            if position > 0 and position <= len(CDLL):
                CDLL.removeany(position)
            else:
                print("Invalid position!")
        elif n == 7:
            key = eval(input("Enter the key : "))
            CDLL.search(key)
        elif n == 8:
            CDLL.display()
        elif n == 9:
            print("The size of the CDLL is :", len(CDLL))
        elif n == 10:
            print("Exiting....")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()