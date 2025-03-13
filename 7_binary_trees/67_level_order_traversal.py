print("\n.........................Implementing Level order Traversal in Binary Trees.........................\n")


from queue_using_array import QueuesArray
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

    def levelorder(self):
        q = QueuesArray()
        t = self._root
        q.enqueue(t)
        print(t._element, end=" ")
        while not q.isempty():
            t = q.dequeue()
            if t._left:
                print(t._left._element, end=" ")
                q.enqueue(t._left)
            if t._right:
                print(t._right._element, end=" ")
                q.enqueue(t._right)


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

print("Level-order Traversal:", end=" ")
t.levelorder()




#creating the following binary tree
#         5
#       /   \
#     3      8
#    / \       \
#   1   4       6

        
