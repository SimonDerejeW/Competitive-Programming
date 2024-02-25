# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.summ = 0
        self.s = ""
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 
            self.s += str(root.val)
            if root.left is None and root.right is None:
                self.summ += int(self.s)
            else:
                helper(root.left)
                helper(root.right)

            self.s = self.s[:-1]


        helper(root)
        return self.summ
        

        