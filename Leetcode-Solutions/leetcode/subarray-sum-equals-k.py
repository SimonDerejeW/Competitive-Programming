class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        summ = 0
        res = []
        maxSub = 0
        # for i in range(len(nums)):
        #     summ += nums[i]
        #     res.append(summ)
        # # print(res)

        # for i in range(len(res)):
        #     prefix[res[i]] = 1 + prefix.get(res[i], 0)
        # print(prefix)
        anotherSum = 0
        for i in range(len(nums)):
            anotherSum += nums[i]
            diff = anotherSum - k
            maxSub += prefix.get(diff,0)
            prefix[anotherSum] = 1 + prefix.get(anotherSum, 0)

        return maxSub
