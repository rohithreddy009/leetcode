from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums: 
            # temp = n * curr_max
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(n * curr_max, n * curr_min, n )
            res = max(res, curr_max)
        return res
        
# print(Solution().maxProduct([2, 3, -2, 4]))  # Output: 6
print(Solution().maxProduct([-4, -3, -2]))  # Output: 0