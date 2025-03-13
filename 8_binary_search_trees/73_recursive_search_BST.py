print("\n.........................Searching an element using Recursive function in Binary Search Tree.........................\n")

class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def recursive_insert(self, root, element):
        if root is None:
            return _Node(element)
        if element == root._element:
            print("Element already exists")
            return root
        elif element <  root._element:
            root._left = self.recursive_insert(root._left, element)
        elif element > root._element:
            root._right = self.recursive_insert(root._right, element)
        return root
    
    def insert(self, element):
        if self._root:
            self._root = self.recursive_insert(self._root, element)
        else:
            self._root = _Node(element)

    def recursive_search(self, root, element):
        if root is None:
            return False
        if element == root._element:
            return True
        elif element < root._element:
            return self.recursive_search(root._left, element)
        elif element > root._element:
            return self.recursive_search(root._right, element)
        return False
    
    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end=" ")
            self.inorder(root._right)



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

print("5 is present in above BST:", BST.recursive_search(BST._root, 5))
print("7 is present in above BST:", BST.recursive_search(BST._root, 7))

#creating the following binary tree
#         5
#       /   \
#      3     8
#     / \   / \
#    1   4 6   9
