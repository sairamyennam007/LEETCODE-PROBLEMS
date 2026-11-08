# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def isvalid(v,min,max):
            if not v:
                return True
            if not min<v.val<max:
                return False
            return isvalid(v.left,min,v.val) and isvalid(v.right,v.val,max)
        return isvalid(root,float('-inf'),float('+inf'))