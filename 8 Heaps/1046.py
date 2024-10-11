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


