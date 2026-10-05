# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            leftLength = dfs(node.left)
            rightLength = dfs(node.right)
            maxLength = max(leftLength, rightLength)

            if abs(leftLength - rightLength) > 1:
                balanced = False

            return 1 + maxLength

        dfs(root)
        return balanced