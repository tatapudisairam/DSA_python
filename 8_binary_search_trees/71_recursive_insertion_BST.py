print("\n.........................Inserting node using Recursive function in Binary Search Tree.........................\n")


class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def recursive_insert(self, troot, element):
        if troot is None:
            return _Node(element)
        if element == troot._element:
            print("Element already exists")
            return troot
        elif element < troot._element:
            troot._left = self.recursive_insert(troot._left, element)
        elif element > troot._element:
            troot._right = self.recursive_insert(troot._right, element)
        
        return troot
        
    def insert(self, element):
        if self._root:
            self._root = self.recursive_insert(self._root, element)
        else:
            self._root = _Node(element)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)



BST = BinarySearchTree()

BST.insert(5)
BST.insert(3)
BST.insert(8)
BST.insert(6)
BST.insert(1)
BST.insert(9)

print("Inorder:")
BST.inorder(BST._root)


#creating the following binary tree
#         5
#       /   \
#      3     8
#     /     / \
#    1     6   9
