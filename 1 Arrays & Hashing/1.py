class Solution:
    def twoSum(self, nums, target):
        hmap = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hmap:
                return [i, hmap[diff]]
            hmap[v] = i

a = Solution()
print(a.twoSum([2,7,11,15],26))