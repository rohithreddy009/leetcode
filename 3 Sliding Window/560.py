from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    res += 1
        return res

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in hmap:
                res += hmap[prefix_sum - k]
            
            hmap[prefix_sum] += 1
        
        return res

print(Solution2().subarraySum([1,2,3,4,5], 5))  