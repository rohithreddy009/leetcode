from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            for row_inc, col_inc in directions:
                dfs(r + row_inc, c + col_inc, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

a = Solution()
# print(a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(a.pacificAtlantic([
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]))

        