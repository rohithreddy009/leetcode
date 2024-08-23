from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != fast:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow2

a = Solution()
print(a.findDuplicate([1,3,4,2,2]))