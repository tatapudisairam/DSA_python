print("\n.........................Finding height of Binary Tree.........................\n")

class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right
    
class BinaryTree:
    def __init__(self):
        self._root = None
    
    def maketree(self, element, left, right):
        self._root = _Node(element, left._root, right._root)
    
    def height(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x>y:
                return x+1
            else:
                return y+1
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


print("Height of the tree is:", t.height(t._root)-1) # since the height starts from 0




#creating the following binary tree
#         5
#       /   \
#     3      8
#    / \       \
#   1   4       6
