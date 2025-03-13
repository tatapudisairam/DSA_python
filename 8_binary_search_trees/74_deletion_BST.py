print("\n.........................Deleting an element from Binary Search Tree (Min value from right subtree).........................\n")


class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right
    
class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def inserting(self, root, element):
        if not root:
            return _Node(element)
        if element == root._element:
            print("Element already exists")
            return root
        elif element < root._element:
            root._left = self.inserting(root._left, element)
        elif element > root._element:
            root._right = self.inserting(root._right, element)
        return root
        
    def insert(self, element):
        if self._root:
            self._root = self.inserting(self._root, element)
        else:
            self._root = _Node(element)

    def preorder(self, root):
        if root:
            print(root._element, end=" ")
            self.preorder(root._left)
            self.preorder(root._right)

    # The trick is to find the inorder successor of the node
    def minValue(self, root):
        while root._left:
            root = root._left
        return root


    def deleting(self, root, element):
        if root is None:
            print("Element doesn't exists")
            return root
        if element < root._element:
            root._left = self.deleting(root._left, element)
        elif element > root._element:
            root._right = self.deleting(root._right, element)
        else:
            if root._left is None:
                return root._right
            if root._right is None:
                return root._left
            temp = self.minValue(root._right) # The trick is to find the inorder successor of the node
            root._element = temp._element
            root._right = self.deleting(root._right, temp._element)

        return root
    
    def delete(self, element):
        if self._root:
            self._root = self.deleting(self._root, element)
        else:
            print("Tree doesn't exists")



BST = BinarySearchTree()

BST.insert(5)
BST.insert(3)
BST.insert(8)
BST.insert(6)
BST.insert(1)
BST.insert(4)
BST.insert(9)

print("Pre-Order:", end=" ")
BST.preorder(BST._root)
print()

BST.delete(8)
print("After Deleting Node-8, pre-order traversal is:", end=" ")
BST.preorder(BST._root)
print()

#creating the following binary tree
#         5
#       /   \
#      3     8
#     / \   / \
#    1   4 6   9
