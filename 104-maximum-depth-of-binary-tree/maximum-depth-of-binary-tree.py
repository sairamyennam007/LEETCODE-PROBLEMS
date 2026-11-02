# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        else:
            l=root
            def depth(l):
                if l.left and l.right:
                    return 1 + max(depth(l.left),depth(l.right))
                elif l.left and not l.right:
                    return 1+depth(l.left)
                elif not l.left and l.right:
                    return 1+depth(l.right)
                else:
                    return 1

            return depth(root)
            

                

        