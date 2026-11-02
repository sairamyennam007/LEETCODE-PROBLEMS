# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        l=root
        r=root
        def issame(l,r):
            if not l and not r :
              return True
            elif not l or not r:
                return False
            elif l.val!=r.val:
              return False
            else:
                return  issame(l.left,r.right) and issame(l.right,r.left)
        return issame(l,r)