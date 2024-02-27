# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # count = 0
        # def inorder(root,count):
        #     if root is None:
        #         return
        #     if count == k:
        #         return root
            
        #     inorder(root.left,count)
        #     count += 1
        #     inorder(root.right,count)
        # return inorder(root,0)
        ans = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans[k - 1]