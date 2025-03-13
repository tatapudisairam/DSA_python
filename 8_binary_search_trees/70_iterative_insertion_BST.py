print("\n.........................Inserting node using Iterative function in Binary Search Tree.........................\n")

class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None
    

    def iterative_insert(self, troot, element):
        if troot is None:
            self._root = _Node(element)
            return
        temp = None
        while troot:
            temp = troot
            if element == troot._element:
                print("Element already exists")
                return
            elif element < troot._element:
                troot = troot._left
            elif element > troot._element:
                troot = troot._right
        if element < temp._element:
            temp._left = _Node(element)
        elif element > temp._element:
            temp._right = _Node(element)

    # def iterative_insert(self, troot, element):
    #     temp = None
    #     if troot:
    #         while troot:
    #             temp = troot
    #             if element == troot._element:
    #                 print("Element already exists")
    #                 return
    #             elif element<troot._element:
    #                 troot = troot._left
    #             elif element>troot._element:
    #                 troot = troot._right
            
    #         if element<temp._element:
    #             temp._left = _Node(element)
    #         elif element>temp._element:
    #             temp._right = _Node(element)
    #     else:
    #         self._root = _Node(element)


    def insert(self, element):
        self.iterative_insert(self._root, element)

    def inorder_traversal(self, troot):
        if troot:
            self.inorder_traversal(troot._left)
            print(troot._element, end=" ")
            self.inorder_traversal(troot._right)
    
    def inorder(self):
        if self._root:
            self.inorder_traversal(self._root)
        else:
            print("Tree is empty")

BST = BinarySearchTree()

BST.insert(5)
BST.insert(3)
BST.insert(8)
BST.insert(6)
BST.insert(1)
BST.insert(4)
BST.insert(9)

print("Inorder Traversal:")
BST.inorder()


#creating the following binary tree
#         5
#       /   \
#      3     8
#     / \   / \
#    1   4 6   9
