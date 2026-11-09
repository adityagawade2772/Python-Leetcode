# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solveBinaryTree(self, node,p,q):
        if node == None:
            return None
        if node==p or node==q:
            return node
        left = self.solveBinaryTree(node.left,p,q)
        right = self.solveBinaryTree(node.right, p,q)
        if left != None and right!= None:
            return node
        elif(left is None):
            return right
        elif(right is None):
            return left
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solveBinaryTree(root, p,q)
        