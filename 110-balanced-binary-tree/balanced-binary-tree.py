# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        if root is None:
            return True
        l=self.depth(root.left)
        r=self.depth(root.right)
        if abs(l-r)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self,root):
            if root is None:
                return 0
            l=self.depth(root.left)
            r=self.depth(root.right)
            return 1+max(l,r)
        
            
        