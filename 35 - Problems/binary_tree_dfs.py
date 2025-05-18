# Binary tree Depth first Search

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,value):
        self.root = Node(value)

    # root -> left -> right
    def preorder(self,start,traversal): # pre-order traversal
        if start is None:
            return
        
        traversal.append(start.value)
        self.preorder(start.left,traversal)
        self.preorder(start.right,traversal)

        return traversal
    
    # left -> root -> right
    def inorder(self,start,traversal): # in-order traversal
        if start is None:
            return
        
        self.inorder(start.left,traversal)
        traversal.append(start.value)
        self.inorder(start.right,traversal)

        return traversal
    
    # left -> right -> root
    def postorder(self,start,traversal): # post-order traversal
        if start is None:
            return
        
        self.postorder(start.left,traversal)
        self.postorder(start.right,traversal)
        traversal.append(start.value)

        return traversal


tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(f"Pre-Order result = {tree.preorder(tree.root,[])}")
print(f"In-Order result = {tree.inorder(tree.root,[])}")
print(f"Post-Order result = {tree.postorder(tree.root,[])}")