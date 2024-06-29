from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
            else:
                l = r
            r += 1
        return maxProfit
    
a = Solution()
print(a.maxProfit([7,1,5,3,6,4,0,7]))