from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = defaultdict(int)

        for n in nums:
            hmap[n] += 1
        
        for i in hmap:
            if hmap[i] == 1:
                return i

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

print(Solution2().singleNumber([4, 1, 2, 1, 2]))  # Output: 4