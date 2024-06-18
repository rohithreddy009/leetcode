from typing import List

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length = len(nums)
        # ans = [1] * length
        # for i in range(length):
        #     product = 1
        #     for j in range(length):
        #         if i != j:
        #             product *= nums[j]
        #     ans[i] = product
        # return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    
solution = Solution()

print(solution.productExceptSelf([1,2,3,4]))