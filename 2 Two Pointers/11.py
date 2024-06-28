from typing import List

# class Solution1:
#     def maxArea(self, nums: List[int]) -> int:
#         res = 0
#         for l in range(len(nums)):
#             for r in range(l+1, len(nums)):
#                 area = (r - l) * min(nums[l], nums[r])
#                 res = max(res, area)
#         return res
    

# a = Solution1()
# print(a.maxArea([1,8,6,2,5,4,8,3,7]))


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while(l < r):
            currSol = (r-l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else: 
                l += 1  
            res = max(res, currSol)
        return res
    
b =  Solution2()
print(b.maxArea([1,8,6,2,5,4,8,3,7]))


