class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(l, r):
            curr_res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_res += 1
                l -= 1
                r += 1
            return curr_res
        
        res = 0
        for i in range(len(s)):
            res += count(i, i)
            res += count(i, i+1)
        return res

print(Solution().countSubstrings("abc"))  # Output: 3
# print(Solution().countSubstrings("aaa"))  # Output: 6
# print(Solution().countSubstrings("ababa"))  # Output: 9