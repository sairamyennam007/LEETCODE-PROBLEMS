# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=[]
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
      res=[]
      def order(r):
        if r is None:
            return 
        l=order(r.left)
        res.append(r.val)
        ri=order(r.right)
      order(root)
      return res