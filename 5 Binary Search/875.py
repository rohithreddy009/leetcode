from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            hours = 0

            for i in piles:
                hours += math.ceil(i / mid)
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

a = Solution()
print(a.minEatingSpeed([3,6,7,11],8))