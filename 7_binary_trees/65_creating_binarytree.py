print("\n.........................Creating a simple Binary Tree.........................\n")

class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None
    
    def maketree(self, element, left, right):
        self._root = _Node(element, left._root, right._root)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
dummy = BinaryTree()


x.maketree(40, dummy, dummy)
y.maketree(50, dummy, dummy)
z.maketree(60, dummy, dummy)
r.maketree(20, x, dummy)
s.maketree(30, y, z)
t.maketree(10, r, s) # this is the main root of the tree

# printing the elements of the binary tree using inorder traversal
print("Inorder Traversal: ")
t.inorder(t._root)



#creating the following binary tree
#         10
#       /   \
#     20     30
#    /      /  \
#  40      50   60