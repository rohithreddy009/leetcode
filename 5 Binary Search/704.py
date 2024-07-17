from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                r = mid - 1
            elif nums[mid] > target:
                l = mid + 1
            else:
                return mid
        return -1
    
a = Solution()
print(a.search([1,2,3,4,5],3))
