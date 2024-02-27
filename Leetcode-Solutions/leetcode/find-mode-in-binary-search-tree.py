# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        seen = {}
        def inorder(root):
            nonlocal res,seen
            if root is None:
                return
            inorder(root.left)
            seen[root.val] = 1 + seen.get(root.val, 0)
            inorder(root.right)
        inorder(root)
        max_mode = max(seen.values())
        for key in seen:
            if seen[key] == max_mode:
                res.append(key)

        return res
