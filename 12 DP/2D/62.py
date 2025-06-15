# naive recursive
# time: O(2^(m*n)) space: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == j == 0:
                return 1
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            else:
                return dfs(i-1, j) + dfs(i, j-1)
        return dfs(m-1, n-1)

# top down
# time & space: O(m*n)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = { (0,0): 1}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            else:
                if i == j == 0:
                    return 1
                if i < 0 or j < 0 or i >= m or j >= n:
                    return 0
                else:
                    memo[(i,j)] = dfs(i-1, j) + dfs(i, j-1)
                    return memo[(i,j)]
        return dfs(m-1, n-1)

# bottom up
# time: O(m*n) space: O(m*n)
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([0] * n)
            
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# print(Solution().uniquePaths(2, 3))  # Output: 3
print(Solution3().uniquePaths(3, 7))  # Output: 28