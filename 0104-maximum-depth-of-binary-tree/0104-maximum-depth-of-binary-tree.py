# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recur(self,node):
        if node == None:
            return 0
        left = self.recur(node.left)
        right = self.recur(node.right)
        return 1 + max(left, right)

    def levelorder(self, root):
        if root is None:
            return 0
        queue = deque([])
        height = 0
        queue.append(root)
        while len(queue)!=0:
            level_size = len(queue)
            height+= 1
            for _ in range(level_size):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
        return height
    def maxDepth(self, root: TreeNode | None) -> int:
        a = self.levelorder(root)
        return a        