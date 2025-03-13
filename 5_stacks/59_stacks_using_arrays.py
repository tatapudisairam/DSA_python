print("\n.........................Implementation of Stacks using Arrays.........................\n")

# here we are using python's list class to store elements of the stack and the size of the list need not be defined and the size of the list grows as the elements are inserted.
# So, we should not be bothered about th estack getting full(Overflow) as the elements are inserted. 
class StacksArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)
        

    def pop(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        return self._data.pop()
        
    def peek(self):
        if self.isempty():
            print("Stack Underflow!")
            return
        return self._data[-1]

def main():
    s = StacksArray()
    
    while True:
        print("\nChoose an option:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Top of the stack")
        print("4. Display the stack")
        print("5. length of the stack")
        print("6. isEmpty ?")
        print("7. Exit")  

        n = int(input("Enter you choice: "))

        if n == 1:
            ele = input("Enter the element: ")
            if ele.isdigit() or ele.replace(".", "").isdigit():
                ele = eval(ele)
            s.push(ele)
            print("Added")
        elif n == 2:
            print("The removed element is:", s.pop())
        elif n == 3:
            print("The top of the stack is:", s.peek())
        elif n == 4:
            print("The stack is:", s._data)
        elif n == 5:
            print("The length of the stack:", len(s))
        elif n == 6:
            print(s.isempty())
        elif n == 7:
            print("Exiting....")
            break
        else:
            print("Invalid choice, try again!")


if __name__=='__main__':
    main()
        
         