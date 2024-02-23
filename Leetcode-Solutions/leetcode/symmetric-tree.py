# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dummy = root
        def isSym(root,dummy):
            if (root is None and dummy) or (dummy is None and root):
                self.ans = False
                return self.ans

            if dummy is None and root is None:
                return self.ans

            if dummy.val != root.val:
                self.ans = False
                return self.ans

            print(dummy.val, root.val)
            isSym(root.right,dummy.left)
            isSym(root.left,dummy.right)

            return self.ans
        return isSym(root , dummy)
        
        