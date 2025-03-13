print("\n.........................Searching an element using Iterative function in Binary Search Tree.........................\n")

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
        # if troot is None:
        #     self._root = _Node(element)
        temp = None
        while troot:
            temp  = troot
            if element == troot._element:
                print("Element already exists")
                return
            elif element < troot._element:
                troot = troot._left
            elif element > troot._element:
                troot = troot._right
        
        if temp._element < element:
            temp._right = _Node(element)
        elif temp._element > element:
            temp._left = _Node(element)


    def insert(self, element):
        if self._root:
            self.iterative_insert(self._root, element)
        else:
            self._root = _Node(element)

    def search(self, element):
        if self._root is None:
            return False
        troot = self._root
        while troot:
            if element == troot._element:
                return True
            elif element<troot._element:
                troot = troot._left
            elif element>troot._element:
                troot = troot._right
        return False

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
BST.insert(4)
BST.insert(9)

print("Inorder:", end=" ")
BST.inorder(BST._root)
print()

print("5 is present in above BST:", BST.search(5))
print("7 is present in above BST:", BST.search(7))

#creating the following binary tree
#         5
#       /   \
#      3     8
#     / \   / \
#    1   4 6   9