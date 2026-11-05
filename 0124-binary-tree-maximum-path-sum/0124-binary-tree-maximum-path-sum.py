# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node):
        if node == None :
            return 0
        left = self.solve(node.left)
        if left < 0:
            left =0
        right = self.solve(node.right)
        if right < 0:
            right = 0
        self.maxi = max(self.maxi, left + node.val +right)
        return node.val + max(left , right)
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi = float("-inf")
        self.solve(root)
        return self.maxi


        