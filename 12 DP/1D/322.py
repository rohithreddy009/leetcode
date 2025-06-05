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

print(Solution().coinChange([1, 2, 5], 11))  # Output: 3