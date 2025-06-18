from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0] = max profit on day i if we cannot buy (i.e., we just sold or did nothing)
        # dp[i][1] = max profit on day i if we can buy
        dp = [[0] * 2 for _ in range(n + 2)]  # +2 to avoid index errors for i+2
        
        # We fill the dp table backwards from the last day
        for day in range(n - 1, -1, -1):
            # If we can buy today
            buy_profit = max(
                -prices[day] + dp[day + 1][0],  # Buy today, can't buy tomorrow
                dp[day + 1][1]                  # Skip today, still can buy tomorrow
            )
            
            # If we can sell today
            sell_profit = max(
                prices[day] + dp[day + 2][1],  # Sell today, cooldown one day
                dp[day + 1][0]                 # Skip today, can still sell tomorrow
            )
            
            dp[day][1] = buy_profit
            dp[day][0] = sell_profit
        
        # We start with the ability to buy
        return dp[0][1]

print(Solution().maxProfit([1, 2, 3, 0, 2]))  # Example test case