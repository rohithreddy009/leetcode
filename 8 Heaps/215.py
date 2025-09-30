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

class Solution3: # QuickSelect
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   # convert kth largest → kth smallest

        def quickSelect(l, r):
            pivot, p = nums[r], l

            # Partition step
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Move pivot to final position
            nums[p], nums[r] = nums[r], nums[p]

            # Recurse into the correct side
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


print(Solution3().findKthLargest([3, 0, 2, 1, 7, 6, 5, 8, 4], 6))