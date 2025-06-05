class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1  # actual start and end of the palindrome

        start, end = 0, 0

        for i in range(len(s)):
            l1, r1 = expand(i, i)       # Odd-length palindrome
            if r1 - l1 > end - start:
                start, end = l1, r1

            l2, r2 = expand(i, i + 1)   # Even-length palindrome
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]

print(Solution().longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(Solution().longestPalindrome("cbbd"))   # Output: "bb"