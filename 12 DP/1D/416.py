from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        
        for i in nums:
            temp_set = dp.copy()
            for j in dp:
                if j + i == target:
                    return True
                temp_set.add(j + i)
            dp = temp_set
        
        return True if target in dp else False

print(Solution().canPartition([1, 5, 11, 5]))  # True