print("\n.........................Inserting in AVL Tree (LL, RR, LR, RL).........................\n")

class _Node:
    __slots__ = '_element', '_left', '_right', '_height'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right
        self._height = 1

class AVLTree:
    def __init__(self):
        self._root = None
    
    def preorder(self, troot):
        if troot:
            print(troot._element, end=" ")
            self.preorder(troot._left)
            self.preorder(troot._right)
        
    def height(self, root):
        if root:
            return root._height
        return 0
    def left_rotate(self, x):
        y = x._right
        z = y._left

        # rotation
        y._left = x
        x._right = z

        # update heights
        x._height = 1 + max(self.height(x._left), self.height(x._right))
        y._height = 1 + max(self.height(y._left), self.height(y._right))

        return y

    def right_rotate(self, x):
        y = x._left
        z = y._right

        # rotation
        y._right = x
        x._left = z

        x._height = 1 + max(self.height(x._left), self.height(x._right))
        y._height = 1 + max(self.height(y._left), self.height(y._right))

        return y

    def balance(self, root):
        if root:
            return self.height(root._left) - self.height(root._right)
        return 0

    def inserting(self, root, element):
        if root is None:
            return _Node(element)
        if element == root._element:
            print("Element already exists")
            return root
        elif element < root._element:
            root._left = self.inserting(root._left, element)
        elif element > root._element:
            root._right = self.inserting(root._right, element)
        
        root._height = 1 + max(self.height(root._left), self.height(root._right))

        balance = self.balance(root)

        if balance < -1 and element > root._right._element:
            return self.left_rotate(root)
        
        if balance > 1 and element < root._left._element:
            return self.right_rotate(root)

        if balance < -1 and element < root._right._element:
            root._right = self.right_rotate(root._right)
            return self.left_rotate(root)

        if balance > 1 and element > root._left._element:
            root._left = self.left_rotate(root._left)
            return self.right_rotate(root)

        return root

    def insert(self, element):
        if self._root:
            self._root = self.inserting(self._root, element)
        else:
            self._root = _Node(element)

    def height_of_tree(self, root):
        if root:
            x = self.height_of_tree(root._left)
            y = self.height_of_tree(root._right)
            if x > y:
                return x+1
            else:
                return y+1
        else:
            return 0


AVL = AVLTree()

# Right-Right(RR) Case Used here
AVL.insert(30)
AVL.insert(60)
AVL.insert(90)
print("Firstly inserting 30, 60, 90:")
print("Pre order:", end=" ")
AVL.preorder(AVL._root)
print("\nAfter performing rotation Height of the tree is:", AVL.height_of_tree(AVL._root))
print()

# Right-Left(RL) Case Used here
AVL.insert(99)
AVL.insert(95)
print("After inserting 99, 95 in the above tree:")
print("Pre order:", end=" ")
AVL.preorder(AVL._root)
print("\nAfter performing rotation Height of the tree is:", AVL.height_of_tree(AVL._root))
print()

# Left-Left(LL) Case Used here
AVL.insert(20)
AVL.insert(65)
AVL.insert(62)
print("After inserting 20, 65, 62 in the above tree:")
print("Pre order:", end=" ")
AVL.preorder(AVL._root)
print("\nAfter performing rotation Height of the tree is:", AVL.height_of_tree(AVL._root))
print()

# Left-Right(LR) Case Used here
AVL.insert(94)
print("After inserting 94 in the above tree:")
print("Pre order:", end=" ")
AVL.preorder(AVL._root)
print("\nAfter performing rotation Height of the tree is:", AVL.height_of_tree(AVL._root))

#    30  ---->    30      ---->    30         ---->   Performing Right-Right Rotation Case at 30 (Left rotation)      60
#                   \                \                                                                               /  \
#                    60               60                                                                            30   90
#                                       \
#                                        90
# ------------------------------------------------------------------------------------------------------------------

#    60       ---->     60           ---->   Performing Right-Left Rotation Case at 90 (Dual rotation)         60
#   /  \               /  \                                                                                   /  \
#  30   90           30    90                                                                                30   95
#                            \                                                                                   /  \
#                            99                                                                                 90   99
#                           /
#                          95
# ------------------------------------------------------------------------------------------------------------------

#    60       ---->       60        ---->   Performing Left-Left Rotation Case at 90 (Right rotation)         60
#   /  \                 /  \                                                                                /  \
#  30   95              30   95                                                                             30   95
#      /  \            /    /  \                                                                           /    /  \
#     90  99          20   90  99                                                                         20   65   99
#                         /                                                                                   /  \
#                        65                                                                                  62  90
#                       /
#                      62
# ------------------------------------------------------------------------------------------------------------------

#     60       ---->       60        ---->   Performing Left-Right Rotation Case at 95 (Dual rotation)         60
#    /  \                 /  \                                                                                /  \
#   30   95              30   95                                                                             30   90
#  /    /  \            /    /  \                                                                           /    /  \
# 20   65   99         20   65  99                                                                         20   65   95
#     /  \                 /  \                                                                                /    /  \
#    62   90              62   90                                                                             62   94  99
#                                \
#                                 94
# ------------------------------------------------------------------------------------------------------------------