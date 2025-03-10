from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        
        def bfs(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                grid[row][col] = 2
                q.append([row, col])
                return True
            else:
                return False
     
        while q and fresh > 0:
            len_q = len(q)
            for i in range(len_q):
                r, c = q.popleft()
                for row_inc, col_inc in directions:
                    if bfs(r + row_inc, c + col_inc):
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

a = Solution()
print(a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
                

        