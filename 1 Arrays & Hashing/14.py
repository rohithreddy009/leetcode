from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res[:i]
        return res

print(Solution().longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"