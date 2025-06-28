class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        hmap = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in hmap:
                return hmap[(i, j)]
            if s[i] == t[j]:
                hmap[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                hmap[(i,j)] = dfs(i+1, j)
            return hmap[(i,j)]
        
        return dfs(0,0)
            
print(Solution().numDistinct("rabbbit", "rabbit"))  # Output: 3