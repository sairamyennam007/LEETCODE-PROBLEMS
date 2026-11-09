# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        c=0
        def inorder(r):
            nonlocal c
            if not r:
                return None
            l=inorder(r.left)
            c+=1
            if c==k:
                return r.val
            r=inorder(r.right)
            if l is not None:
                return l
            return r
        return inorder(root)

            