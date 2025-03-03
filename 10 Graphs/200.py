from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)] 

        def set_island_zeros(grid, row, col):
            if (0 <= row < ROWS) and (0 <= col < COLS) and grid[row][col] == "1":
                grid[row][col] = "0"
            
                for row_inc, col_inc in directions:
                    set_island_zeros(grid, row + row_inc, col + col_inc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    num_islands += 1
                    set_island_zeros(grid, row, col)
        
        return num_islands

a = Solution() 
print(a.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # 3