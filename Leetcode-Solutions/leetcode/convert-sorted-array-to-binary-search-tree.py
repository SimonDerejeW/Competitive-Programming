# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums):
            if len(nums) == 0:
                return
            
            idx = len(nums) // 2

            root = TreeNode(nums[idx])
            root.left = helper(nums[:idx])
            root.right = helper(nums[idx + 1:])

            return root
        return helper(nums)