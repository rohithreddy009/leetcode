from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= end:
                end = i
        
        return True if end == 0 else False

print(Solution().canJump([2, 3, 1, 1, 4]))  # True