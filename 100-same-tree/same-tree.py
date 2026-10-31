# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        def samet(p,q):
            if not p and not q:
                return True
            elif not p and q or p and not q or p.val != q.val:
                return False
            else:
                return samet(p.left,q.left) and samet(p.right,q.right)
        return samet(p,q)