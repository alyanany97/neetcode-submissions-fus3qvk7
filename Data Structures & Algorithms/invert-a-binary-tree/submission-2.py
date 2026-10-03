# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque #-->double ended queue

#BFS = popleft removes from the leftmost of the list
#DFS = pop() removes from the rightmost of the list

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = []
        queue.append(root)

        queue = deque(queue) #create a list with JUST the root in it, and then turn that list into a queue

        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
            
