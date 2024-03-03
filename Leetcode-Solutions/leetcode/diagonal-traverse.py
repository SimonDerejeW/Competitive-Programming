class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        curr_row = curr_col = 0
        going_up = True

        res = []
        
        while len(res) < (row * col):
            if going_up:
                while curr_row >= 0 and curr_col < col:
                    res.append(mat[curr_row][curr_col])

                    curr_row -= 1
                    curr_col += 1
                
                #When it's out of bounds: There will be two cases

                if curr_col == col:
                    curr_row += 2
                    curr_col -= 1
                else:
                    curr_row += 1
                
                going_up = False
            
            else:
                while curr_col >= 0 and curr_row < row:
                    res.append(mat[curr_row][curr_col])

                    curr_row += 1
                    curr_col -= 1
                
                #When it's out of bounds: There will be two cases

                if curr_row == row:
                    curr_col += 2
                    curr_row -= 1
                else:
                    curr_col += 1
                
                going_up = True

        
        return res


