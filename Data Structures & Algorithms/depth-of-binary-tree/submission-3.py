# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftLength = self.maxDepth(root.left)
        rightLength = self.maxDepth(root.right)

        maxLength = max(leftLength, rightLength)

        return 1 + maxLength