# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_node = float("-inf")
        min_node = float("inf")
        diff = 0
        def ancestorDiff(root,max_node,min_node):
            nonlocal diff
            if root:
                max_node = max(max_node,root.val)
                min_node = min(min_node,root.val)
                diff = max(diff, max_node - min_node)
                ancestorDiff(root.right,max_node,min_node)
                ancestorDiff(root.left,max_node,min_node)


        ancestorDiff(root,max_node,min_node)
        return diff
