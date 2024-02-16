class Solution:
    def minimumSteps(self, s: str) -> int:
        lis = list(s)
        left, right = 0,1
        swaps = 0
        if len(s) == 1:
            return 0
        while left < len(lis) and right < len(lis):
            if lis[left] == "1" and lis[right] == "0":
                lis[left] , lis[right] = lis[right] , lis[left]
                swaps += right - left
                left += 1
                right += 1
            elif lis[left] == "0":
                left += 1
                right += 1
            elif lis[right] == "1":
                right += 1
            
        return swaps
            


