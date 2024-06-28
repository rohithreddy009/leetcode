from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([ nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
a = Solution()

print(a.threeSum([-1,0,1,2,-1,-4]))
