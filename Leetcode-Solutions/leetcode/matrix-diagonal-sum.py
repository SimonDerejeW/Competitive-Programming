class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if col == row:
                    summ += mat[row][col]
        for row in range(len(mat)):
            for col in range(len(mat[0]) - 1, -1, -1):
                if len(mat[0]) - 1 - col == row:
                    summ += mat[row][col]
        
        if len(mat) % 2 != 0:
            x = len(mat) // 2
            return summ - mat[x][x]
        return summ
        