# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def construct(nums):
            if len(nums) == 0:
                return
            mx = nums.index(max(nums))
            
            root = TreeNode(nums[mx])
            root.left = construct(nums[:mx])
            root.right = construct(nums[mx + 1:])

            return root
        
        return construct(nums)