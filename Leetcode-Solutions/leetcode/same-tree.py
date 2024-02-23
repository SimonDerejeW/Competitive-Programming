# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q) or (q is None and p):
            self.ans = False
            return self.ans
        if p is None and q is None:
            return self.ans
        if p.val != q.val:
            self.ans = False
            return self.ans
        
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)

        return self.ans
        


        
        
        
