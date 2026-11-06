# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reversepostorder(self, node, level, ans):
        if node == None:
            return
        if len(ans) == level :
            ans.append(node.val)
        if node.right:
            self.reversepostorder(node.right, level+1,ans)
        if node.left:
            self.reversepostorder(node.left, level +1,ans)
        
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []  
        a = self.reversepostorder(root,0,ans)   
        return ans
        """    
        que = deque()
        result = []
        que.append(root)
        if root == None:
            return result
        while que:
            level_size = len(que)
            for i in range(level_size):
                node = que.popleft()
                if i == level_size-1:
                    result.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result
        """