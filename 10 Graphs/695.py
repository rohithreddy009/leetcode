from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        seen = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col):
            if (0 <= row < ROWS) and (0 <= col < COLS) and grid[row][col] == 1 and (row, col) not in seen:
                seen.add((row, col))
                area = 1
                for row_inc, col_inc in directions:
                    area += dfs(row + row_inc, col + col_inc)
                return area
            else:
                return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area

a = Solution()
print(a.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]))