from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                length = 0
                while n+length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
sol = Solution()

print(sol.longestConsecutive([100,4,200,1,3,2]))