from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(r, c, direction):
            if ( 0 <= r < ROWS and 0 <= c < COLS and matrix[r][c] != 0 and
            matrix[r][c] != "*" ):
                matrix[r][c] = "*"
                if direction == "U":
                    dfs(r - 1, c, "U")
                elif direction == "D":
                    dfs(r + 1, c, "D")
                elif direction == "R":
                    dfs(r, c + 1, "R")
                elif direction == "L":
                    dfs(r, c - 1, "L")

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    dfs(r - 1, c, "U")
                    dfs(r + 1, c, "D")
                    dfs(r, c + 1, "R")
                    dfs(r, c - 1, "L")
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

print(Solution2().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))  # Output: [[1,0,1],[0,0,0],[1,0,1]]