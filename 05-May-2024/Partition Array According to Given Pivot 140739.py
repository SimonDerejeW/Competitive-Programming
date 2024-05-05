# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        lft=[]
        mid = []
        rgt=[]

        for i in nums:
            if i<pivot:
                lft.append(i)
            elif i== pivot:
                mid.append(i)
            else:
                rgt.append(i)
        lft.extend(mid)
        lft.extend(rgt)
        return lft
        