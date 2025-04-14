from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hmap = defaultdict(list)
        visit_set = set()
        res = 0

        for u, v, w in times:
            hmap[u].append((w,v))
        
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visit_set:
                continue
            visit_set.add(node)
            res = max(res, time)

            for weight, neighbor in hmap[node]:
                if neighbor not in visit_set:
                    heapq.heappush(min_heap, (time + weight, neighbor))
        
        return res if len(visit_set) == n else -1

a = Solution()
print(a.networkDelayTime([[1,2,4],[1,3,1],[3,4,1],[4,2,1]], 4, 1)) 
         