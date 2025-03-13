print("\n.........................Counting Number of nodes in Binary Tree.........................\n")

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

    def countnodes(self, troot):
        if troot:
            x = self.countnodes(troot._left)
            y = self.countnodes(troot._right)
            return x+y+1
        else:
            return 0

    

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

print("Number of nodes are:", t.countnodes(t._root))




#creating the following binary tree
#         5
#       /   \
#     3      8
#    / \       \
#   1   4       6
