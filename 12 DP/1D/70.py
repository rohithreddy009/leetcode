class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(x):
            if x >= n:
                return x == n
            return dfs(x+1) + dfs(x+2)
        return dfs(0)
    
    def climbStairsMemo(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]

        return dfs(0)

a = Solution()

print(a.climbStairsMemo(3))  # Output: 8