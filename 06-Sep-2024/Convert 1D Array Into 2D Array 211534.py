# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        x = m*n
        if length < (x) or length > x:
            return []

        arr = [[] for _ in range(m)]
        row = 0
        flag = n
        for num in original:
            if flag == 0:
                row += 1
                flag = n
                arr[row].append(num)
            else:
                arr[row].append(num)
            flag -= 1
        return arr