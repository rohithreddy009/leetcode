from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        curr = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                curr += 1
            
            while curr > k:
                if nums[l] == 0:
                    curr -= 1
                l += 1
            
            window_len = r - l + 1
            res = max(res, window_len)
        
        return res

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
                