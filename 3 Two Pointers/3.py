class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        numSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in numSet:
                numSet.remove(s[l])
                l += 1
            window_len = (r - l) + 1
            res = max(res, window_len)
            numSet.add(s[r])
        return res
        
a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))