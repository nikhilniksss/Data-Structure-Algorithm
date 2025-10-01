# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the 
# farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2


def maxDepth(self,root):
    if not root:
        return 0
    
    right_depth = self.maxDepth(root.right)
    left_depth = self.maxDepth(root.left)
    return 1 + max(right_depth,left_depth)