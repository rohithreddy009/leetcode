from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [ (1,0), (-1,0), (0,1), (0,-1)]
        visit_set = set()
        q = deque()

        def bfs(r, c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] != 2147483647 or (r,c) in visit_set:
                return
            else:
                q.append([r,c])
                visit_set.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit_set.add((r,c))
        
        dist = 0
        while q:
            len_q = len(q)
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