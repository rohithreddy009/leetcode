from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # Memoization for (r, c)

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1  # Minimum path is the cell itself

            for row_inc, col_inc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + row_inc, c + col_inc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        return max(dp.values())

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4