# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            new = ""
            strs = str(num)
            for s in strs:
                new += str(mapping[int(s)])
            arr.append([num, int(new)])
        arr.sort(key = lambda x:x[1])
        
        return [x for x, y in arr]
