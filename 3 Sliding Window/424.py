class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hmap = {}
        res = 0
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            if (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            window_len = r - l + 1
            res = max(res, window_len)
        return res
    
a = Solution()
print(a.characterReplacement("AABABBA",2))
