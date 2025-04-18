from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) # no need of rows, cols bcoz it is square matrix
        visit_set = set()
        min_heap = [[grid[0][0], 0, 0]]
        directions = [ (1,0), (-1,0), (0,1), (0,-1)]

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if r == N-1 and c == N - 1:
                return time
            
            for row_inc, col_inc in directions:
                new_r, new_c = r + row_inc, c + col_inc
                if ( new_r < 0 or new_c < 0 or new_r >= N or new_c >= N 
                or (new_r, new_c) in visit_set):
                    continue
                visit_set.add((new_r, new_c))
                heapq.heappush(min_heap, [max(time, grid[new_r][new_c]), new_r, new_c])

a = Solution()
print(a.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])) 