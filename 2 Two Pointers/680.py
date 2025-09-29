class Solution: # time and space O(n)
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_l, skip_r = s[l+1: r+1], s[l:r]
                if skip_l == skip_l[::-1] or skip_r == skip_r[::-1]:
                    return True
                return False
            l, r = l+1, r-1
        return True


class Solution2: # time O(n) space O(1)
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
                

        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l, r = l+1, r-1
        return True

print(Solution().validPalindrome("aaaza"))