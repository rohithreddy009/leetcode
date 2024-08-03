class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(x):
            return ord('a') <= ord(x) <= ord('z') or ord('A') <= ord(x) <= ord('Z') or ord('0') <= ord(x) <= ord('9') 

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not helper(s[l]):
                l += 1
            while r > l and not helper(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))