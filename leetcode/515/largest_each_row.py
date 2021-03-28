# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            res.append(max(node.val for node in stack))
            stack = [child for node in stack for child in (node.left, node.right)
                     if child]
        return res
        
