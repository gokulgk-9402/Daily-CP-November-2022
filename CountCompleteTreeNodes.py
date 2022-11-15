# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return 0
            
            v1 = helper(node.right)
            v2 = helper(node.left)

            return v1 + v2 + 1

        return helper(root)