print("\n.........................Implementation of Stacks using LinkedList.........................\n")

# it is much better to perform the operations of push and pop operations at the beginning of the linked list
# the time complexity of inserting ang removing at the beginning of single linked list is order of one or O(1)
class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class StacksLinkedList:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
    
    def pop(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        ele = self._top._element
        self._top = self._top._next
        self._size -= 1
        return ele

    def peek(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        return self._top._element
    
    def traverse(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        p = self._top
        print("top", end="")
        while p:
            print(f' -> {p._element}', end="")
            p = p._next


def main():
    s = StacksLinkedList()

    while True:
        print("\nChoose an option:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Top of the stack")
        print("4. Display the stack")
        print("5. length of the stack")
        print("6. isEmpty ?")
        print("7. Exit") 

        n = int(input("Enter your choice: "))

        if n == 1:
            ele = input("Enter the element: ")
            if ele.isdigit() or ele.replace(".", "").isdigit():
                ele = eval(ele)
            s.push(ele)
            print("Added")
        elif n == 2:
            print("The Removed element at the top is:", s.pop())
        elif n == 3:
            print("The top of the stack is:", s.peek())
        elif n == 4:
            print("The stack is: ", end="")
            s.traverse()
        elif n == 5:
            print("The length of the stack is:", len(s))
        elif n == 6:
            print(s.isempty())
        elif n == 7:
            print("Exiting....")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == '__main__':
    main()


