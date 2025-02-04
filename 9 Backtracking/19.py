class Solution:
    def letterCombinations(self, digits: str):
        res = []
        d2c = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return 
            
            for c in d2c[digits[i]]:
                dfs(i+1, curr + c)
        
        if digits:
            dfs(0, "")

        return res

a = Solution()
print(a.letterCombinations("23"))