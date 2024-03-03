class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []

        for rows in range(len(board)):
            for cols in range(len(board[0])):
                if board[rows][cols].isdigit() and board[rows][cols] not in row:
                    row.append(board[rows][cols])
                elif board[rows][cols] in row:
                    # print("Row: ", rows, cols)
                    return False
            row = []

        for cols in range(len(board[0])):
            for rows in range(len(board)):
                if board[rows][cols].isdigit() and board[rows][cols] not in col:
                    col.append(board[rows][cols])
                elif board[rows][cols] in col:
                    # print("Cols: ",rows, cols)
                    return False
            col = []
        
        # box = []
        for i in range(0, 9, 3):  # iterate over rows with step size 3
            for j in range(0, 9, 3):  # iterate over columns with step size 3
                box = []
                for row in range(i, i + 3):  # iterate within a 3x3 box
                    for col in range(j, j + 3):
                        if board[row][col].isdigit() and board[row][col] not in box:
                            box.append(board[row][col])
                        elif board[row][col] in box:
                            # print("Box: ", rows, cols)
                            return False
        return True

                

                
        
