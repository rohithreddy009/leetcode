class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        res, resLen = [-1,-1], float("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                # update the result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # pop from left of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        if resLen != float("infinity"):
            return s[l: r+1]
        else: 
            return ""

a = Solution()
print(a.minWindow("ADOBECODEBANC","ABC"))



