from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        min_index = r

        if min_index == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

a = Solution()
print(a.search([4,5,6,7,0,1,2],4))