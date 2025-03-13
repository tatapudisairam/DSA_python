print("\n.........................Implementing 3 types of Traversal in Binary Trees.........................\n")

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


def inorder(troot):
    if troot:
        inorder(troot._left)
        print(troot._element, end=" ")
        inorder(troot._right)

def preorder(troot):
    if troot:
        print(troot._element, end=" ")
        preorder(troot._left)
        preorder(troot._right)

def postorder(troot):
    if troot:
        postorder(troot._left)
        postorder(troot._right)
        print(troot._element, end=" ")



x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
dummy = BinaryTree()

x.maketree(1, dummy, dummy)
y.maketree(4, dummy, dummy)
z.maketree(6, dummy, dummy)
r.maketree(3, x, y)
s.maketree(8, dummy, z)
t.maketree(5, r, s)

print("Pre-order Traversal:", end=" ")
preorder(t._root)
print()

print("In-order Traversal:", end=" ")
inorder(t._root)
print()

print("Post-order Traversal:", end=" ")
postorder(t._root)
print()




#creating the following binary tree
#         5
#       /   \
#     3      8
#    / \       \
#   1   4       6