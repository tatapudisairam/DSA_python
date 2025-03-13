print("\n.........................Recursion and it's analysis.........................\n")

# tail recursion
print("1. Printing Squares till number n (descending order)")
def printing_squares_tail(n):
    if n>0:
        k = n*n
        print(n , "square =", k)
        printing_squares_tail(n-1)

n = int(input("Enter a number to print the list of squares till that number: "))
printing_squares_tail(n)
print()

# head recursion
print("2. Printing squares till number n (ascending order)")
def printing_squares_head(n):
    if n>0:
        printing_squares_head(n-1)
        k = n*n
        print(n, "square =", k)

n = int(input("Enter a number to print the list of squares till that number: "))
printing_squares_head(n)
print()

# indirect recursion
print("3. Demonstration of Indirect Recursion")
def indirect_1(n):
    if n>0:
        print("Function-1:", n)
        indirect_2(n-1)

def indirect_2(n):
    if n>0:
        print("Function_2:", n)
        indirect_1(n-1)

indirect_1(4)
print()

# tree recursion
print("4. Demonstration of tree recursion")
def tree_recursion(n):
    if n>0:
        tree_recursion(n-1)
        print(n*n)
        tree_recursion(n-1)

tree_recursion(4)
print()