class Solution:
    def combine(self, n: int, k: int):
        res = []

        def dfs(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            for i in range(start, n+1):
                curr.append(i)
                dfs(i+1, curr)
                curr.pop()

        dfs(1,[])
        return res

a = Solution()
print(a.combine(4,2))