from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            return (dfs(i+1, curr_sum + nums[i]) + dfs(i+1, curr_sum - nums[i]))
        
        return dfs(0, 0)

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if i == len(nums):
                return 1 if curr_sum == target else 0

            memo[(i, curr_sum)] = ( dfs(i+1, curr_sum + nums[i]) + 
                                    dfs(i+1, curr_sum - nums[i]) )
            return memo[(i, curr_sum)]
        
        return dfs(0, 0)

print(Solution.findTargetSumWays(Solution, [1, 1, 1], 1))  # Output: 5