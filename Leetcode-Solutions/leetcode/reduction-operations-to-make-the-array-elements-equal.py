class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # length = len(nums)
        # count = 0

        # while len(set(nums))>1:
        #     largest = nums[0]
        #     nextLargest, index = next((item, idx) for idx, item in enumerate(nums) if item != largest)
        #     for j in range(length-index):
        #         nums[j] = nextLargest
        #         count+=1
        #         largest = nextLargest
                
        # return count
        # nums.sort(reverse = True)
        seen = Counter(nums)
        dist = list(set(nums))
        dist.sort(reverse = True)
        
        n = len(dist)
        op = 0
        for i in range(n):
            op += (seen[dist[i]] * (n - i - 1))
        return op

