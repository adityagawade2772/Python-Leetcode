# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node):
        if node == None:
            return 0

        left = self.solve(node.left)
        right = self.solve(node.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left , right)

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        a = self.solve(root)
        return self.diameter
        