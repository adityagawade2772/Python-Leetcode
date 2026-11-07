# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, mini, maxi):
        if node is None:
            return True
        if node.val <= mini or node.val >= maxi:
            return False
        left = self.solve(node.left,mini,node.val)
        right = self.solve(node.right, node.val,maxi)
        return left and right
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.solve(root, float("-inf"),float("inf"))


        
        