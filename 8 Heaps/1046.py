import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def largest():
            largest = stones.index(max(stones))
            return stones.pop(largest)
        
        while len(stones) > 1:
            x = largest()
            y = largest()

            if x != y:
                stones.append(abs(x - y))
            
        return stones[0] if stones else 0


a = Solution()
print(a.lastStoneWeight([2,7,4,1,8,1]))

# # There's a private _heapify_max method.
# # https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
# class Solution(object):
#     def lastStoneWeight(self, stones):
#         heapq._heapify_max(stones)
#         while len(stones) > 1:
#             max_stone = heapq._heappop_max(stones)
#             diff = max_stone - stones[0]
#             if diff:
#                 heapq._heapreplace_max(stones, diff)
#             else:
#                 heapq._heappop_max(stones)
        
#         stones.append(0)
#         return stones[0]
