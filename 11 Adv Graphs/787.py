from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for src, dst, price in flights:  # src=source, dst=dest, price=price
                if prices[src] == float("inf"):
                    continue
                if prices[src] + price < tmpPrices[dst]:
                    tmpPrices[dst] = prices[src] + price
            prices = tmpPrices
            
        return -1 if prices[dst] == float("inf") else prices[dst]

a = Solution()
print(a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)) # 200
print(a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)) # 500
print(a.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)) # 700