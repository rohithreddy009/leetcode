from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                return mid

print(Solution().findPeakElement([1, 2, 3, 1]))  # Output: 2
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 1 or 5