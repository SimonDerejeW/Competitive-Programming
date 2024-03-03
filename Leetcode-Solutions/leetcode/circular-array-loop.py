class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def get_next_index(nums, cur_index, is_positive):
            direction = nums[cur_index] >= 0
            if direction != is_positive:
                return -1
            
            next_index = (cur_index+nums[cur_index])%len(nums)
            if next_index < 0:
                next_index = len(nums) - next_index 
                
            if next_index == cur_index:
                next_index = -1
                
            return next_index
        
        for index in range(len(nums)):
            is_positive = nums[index] >= 0
            fast, slow, = index, index
            while True:
                slow = get_next_index(nums, slow, is_positive)
                fast = get_next_index(nums, fast, is_positive)
                
                if fast != -1:
                    fast = get_next_index(nums, fast, is_positive)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
        return False
                
        