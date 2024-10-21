from typing import List
import heapq

# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity: O(n)
# Extra Space Complexity: O(n)

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)

a = Solution2()
print(a.findKthLargest([3,2,1,5,6,4],2))

class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in range(len(nums)):
            if len(minHeap) < k:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappushpop(minHeap, nums[i])
                # heapq.heappop(minHeap)
        
        return minHeap[0]