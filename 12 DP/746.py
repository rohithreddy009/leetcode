from typing import List

# naive recursive
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(i):
            if i < 2:
                return 0
            return min(dfs(i - 2) + cost[i - 2], dfs(i - 1) + cost[i - 1])
        
        return dfs(n)

# memoization
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = { 0:0, 1:0 }
        
        def dfs(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(dfs(i - 2) + cost[i - 2], dfs(i - 1) + cost[i - 1])
                return memo[i]
        
        return dfs(n)

# bottom-up
class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[n]

print(Solution3().minCostClimbingStairs([10, 15, 20]))  # Output: 15
# print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6