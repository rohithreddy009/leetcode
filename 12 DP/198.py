from typing import List

# top down  
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = { 0: nums[0], 1: max(nums[0], nums[1])}

        def dfs(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
                return memo[i]
        
        return dfs(n-1)

# bottom up
class Solution2:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]

        

print(Solution().rob([2,7,9,3,1]))  # Output: 12