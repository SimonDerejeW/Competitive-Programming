# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
        self.flag = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        root.left = self.isValidBST(root.left)
        if self.arr and self.arr[-1] >= root.val:
            self.flag = False
        
        self.arr.append(root.val)
        root.right = self.isValidBST(root.right)

        # print(self.arr)
        return self.flag
        