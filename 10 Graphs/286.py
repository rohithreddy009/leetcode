from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        q = deque()

        def bfs(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == -1 or (row, col) in visited:
                return 
            visited.add((row, col))
            q.append([row, col])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for row_inc, col_inc in directions:
                    bfs(r + row_inc, c + col_inc)
            dist += 1
        return grid

a = Solution()
result = (a.islandsAndTreasure([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]))  
print(result)