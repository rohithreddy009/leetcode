from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

print(Solution().wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False