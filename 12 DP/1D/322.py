from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            
            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        return -1 if dfs(amount) >= float("inf") else dfs(amount)

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] =0

        for i in range(1, amount +1):
            for coin in coins:
                if (i -coin) >= 0:

                    dp[i] = min(dp[i], 1+ dp[i-coin])

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

print(Solution2().coinChange([1, 2, 5], 6))  # Output: 3