from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [ (1,0), (-1,0), (0,1), (0,-1)]

        # dfs function to check in all 4 directions and convert O to 1
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return 
            board[r][c] = "1"
            for row_inc, col_inc in directions:
                dfs(r + row_inc, c + col_inc)
        
        # left and right borders of the matrix
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        # top and left borders of the matrix
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        
        # iterate the 2D array, change O -> X and 1 -> O 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "1":
                    board[r][c] = "O"
        
        print(board)

a = Solution()
# a.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
a.solve([
    ["X", "X", "X", "O", "X"],
    ["X", "X", "O", "X", "O"],
    ["X", "X", "O", "O", "O"],
    ["O", "X", "X", "X", "X"],
    ["X", "X", "O", "O", "X"],
    ["X", "X", "X", "X", "X"]
])

            
        