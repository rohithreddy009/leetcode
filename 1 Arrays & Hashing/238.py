from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix   
            postfix *= nums[i]
        return res
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = len(nums)
        la = [0] * n
        ra = [0] * n

        for i in range(len(nums)):
            j = -i -1
            la[i] = prefix
            ra[j] = postfix
            prefix *= nums[i]
            postfix *= nums[j]
        
        # for j in range(len(nums)-1,-1,-1):
        #     ra[j] = postfix
        #     postfix *= nums[j]
        
        # return [ l*r for l,r in zip(la, ra)]
        res = []
        for l,r in zip(la, ra):
            res.append(l*r)
        return res
    
    
solution = Solution()
print(solution.productExceptSelf2([1,2,3,4]))