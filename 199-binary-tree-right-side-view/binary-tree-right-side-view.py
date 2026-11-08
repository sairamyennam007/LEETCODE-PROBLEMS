# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        q=deque([root])
        res=[]
        if not root:
            return res
        while q:
          l=len(q)
          for i in range(1,l+1):
            n=q.popleft()
            if i==l:
                res.append(n.val)
            if n.left:
                    q.append(n.left)
            if n.right:
                    q.append(n.right)
        return res
