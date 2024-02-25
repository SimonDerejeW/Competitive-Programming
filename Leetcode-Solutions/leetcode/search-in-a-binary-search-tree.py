# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val > val:
            root.left = self.searchBST(root.left, val)
        elif root.val < val:
            root.right = self.searchBST(root.right, val)
        else:
            self.ans = root
            return root
        return self.ans