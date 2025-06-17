class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            else:
                return max( dfs(i+1, j), dfs(i, j+1))

        return dfs(0, 0)

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            elif i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            else:
                memo[(i,j)] = max( dfs(i+1, j), dfs(i, j+1))
                return memo[(i,j)]
        
        return dfs(0, 0)

class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

print(Solution3().longestCommonSubsequence("gators", "agars"))    # Output: 4
print(Solution2().longestCommonSubsequence("abcde", "ace"))  # Output: 3