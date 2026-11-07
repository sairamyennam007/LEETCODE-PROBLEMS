# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        que=deque([root])
        res=[]
        while que:
            n=len(que)
            lvl=[]
            for i in range(n):
                n1=que.popleft()
                lvl.append(n1.val)      
                if n1.left:
                     que.append(n1.left)
                if n1.right:
                     que.append(n1.right)
            res.append(lvl)
        return res
