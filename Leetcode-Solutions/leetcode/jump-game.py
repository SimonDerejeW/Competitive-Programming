class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if len(nums) > 1 and sum(nums[:-1]) < len(nums)-1:
        #     return False
        # for i in range(len(nums)-1):
        #     if nums[i] == 0 and sum(nums[:i]) < len(nums)-1:
        #         return False
        # return True

        # if 0 not in nums:
        #     return True
        # if len(nums) == 1:
        #     return True
        
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         res.append(i)
        # res = res[-1]
        # print(res)
        
        # for i in range(res):
        #     if nums[i] + i > res:
        #         return True
        #     elif nums[i] + i == res and res == len(nums)-1:
        #         return True
        # return False

        if 0 not in nums:
            return True
        ans = True
        position = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if position - i > nums[i]:
                ans = False
            else:
                position -= position - i
                ans = True
        return ans

            


        


