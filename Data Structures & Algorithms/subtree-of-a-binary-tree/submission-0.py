# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    #isSubTree searches for a possible starting node
    #sameTree checks whether that starting node actually matches subRoot!
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def sameTree(root, subRoot):            
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False

            leftSide = sameTree(root.left, subRoot.left)
            rightSide = sameTree(root.right, subRoot.right)

            return leftSide and rightSide
        
        #check whether subRoot starts HERE
        if sameTree(root, subRoot):
            return True 

        #otherwise search left side and right side
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        #if either side finds it return true
        return left or right