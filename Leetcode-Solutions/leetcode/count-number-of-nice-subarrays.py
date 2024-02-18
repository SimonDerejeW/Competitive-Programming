class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        binary = []
        for i in range(len(nums)):
            if nums[i] %2 != 0:
                binary.append(1)
            else:
                binary.append(0)
        
        seen = {0:1}
        prefixSum = 0
        niceSub = 0
        
        for i in range(len(binary)):
            prefixSum += binary[i]
            diff = prefixSum - k
            niceSub += seen.get(diff,0)
            seen[prefixSum] = 1 + seen.get(prefixSum, 0)

        return niceSub