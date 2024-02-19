class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        sub_count = defaultdict(int)
        dist = len(nums_count)
        # print(dist)
        left = 0
        count = 0
        for right in range(len(nums)):
            sub_count[nums[right]] += 1

            while len(sub_count) == dist:
                count += len(nums) - right
                sub_count[nums[left]] -= 1
                if sub_count[nums[left]] == 0:
                    sub_count.pop(nums[left])
                left += 1
        return count


            