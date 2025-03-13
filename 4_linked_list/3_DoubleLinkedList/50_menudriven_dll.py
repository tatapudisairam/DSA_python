print("\n.........................Menu Driven program of the Double Linked list.........................\n")

class _Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
    
    def addlast(self, element):
        newest = _Node(element, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1
        print("Added")
    
    def addfirst(self, element):
        newest = _Node(element, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._head._prev = newest
            newest._next = self._head
            self._head = newest
        self._size += 1
        print("Added")
    
    def addany(self, element, position):
        if position == 1:
            self.addfirst(element)
            return
        elif position == len(self)+1:
            self.addlast(element)
            return
        newest = _Node(element, None, None)
        p = self._head
        index = 1
        while index < position - 1:
            p = p._next
            index = index+1
        newest._next = p._next
        newest._next._prev = newest
        newest._prev = p
        p._next = newest
        self._size += 1
        print("Added")
    
    def removelast(self):
        if self.isempty():
            print("List is empty")
            return
        elif self._size == 1:
            ele = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            print("The deleted element at end is:", ele)
            return
        ele = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        print("The deleted element at end is:", ele)

    def removefirst(self):
        if self.isempty():
            print("Linked list is empty")
            return
        elif len(self) == 1:
            ele = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            print("The deleted element at beginning is:", ele)
            return
        ele = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        print("The deleted element at beginning is:", ele)

    def removeany(self, position):
        if self.isempty():
            print("List is empty")
            return
        elif position == 1:
            self.removefirst()
            return
        elif position == len(self):
            self.removelast()
            return
        index = 1
        p = self._head
        while index < position-1:
            p = p._next
            index += 1
        ele = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -= 1
        print("The deleted element at position", position, "is: ", ele)

    def search(self, key):
        if self.isempty():
            print("List is empty")
            return
        index = 0
        p = self._head
        while p:
            if p._element == key:
                print(key, "found at index:", index)
                return
            else:
                index += 1
                p = p._next
        print("Element not found")

    def display(self):
        if self.isempty():
            print("Linked list is empty")
            return
        p = self._head
        while p:
            print(p._element, end=' <-> ')
            p = p._next
        print("None")

    def display_reverse(self):
        if self.isempty():
            print("Linked list is empty")
            return
        p = self._tail
        while p:
            print(p._element, end=' <-> ')
            p = p._prev
        print("none")

def main():
    dll = DoubleLinkedList()
    while True:
        print("\nChoose an option:")
        print("1. Add element at the end")
        print("2. Add element at the beginning")
        print("3. Add element at a specific position")
        print("4. Remove an element from the end")
        print("5. Remove an element from the beginning")
        print("6. Remove an element from the a specific position")
        print("7. Display the linked list")
        print("8. Display the linked list in reverse order")
        print("9. Search for an element")
        print("10. Size of the linked list")
        print("11. Exit")   

        n = int(input("Enter your choice: "))
        if n == 1:
            element = eval(input("Enter the element: "))
            dll.addlast(element)
        elif n == 2:
            element = eval(input("Enter teh element: "))
            dll.addfirst(element)
        elif n == 3:
            element = eval(input("Enter the element: "))
            position = int(input("Enter the position: "))
            if position > 0 and position <= len(dll)+1:
                dll.addany(element, position)
            else:
                print("Invalid position")
        elif n == 4:
            dll.removelast()
        elif n == 5:
            dll.removefirst()
        elif n == 6:
            position = int(input("Enter the position: "))
            if position > 0 and position <= len(dll):
                dll.removeany(position)
            else:
                print("Invalid position")
        elif n == 7:
            dll.display()
        elif n == 8:
            dll.display_reverse()
        elif n == 9:
            key = eval(input("Enter the element: "))
            dll.search(key)
        elif n == 10:
            print("The size is:", len(dll))
        elif n == 11:
            print("Exiting....")
            break
        else:
            print("Invalid choice, please try again!")


if __name__ == '__main__':
    main()
