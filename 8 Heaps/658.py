from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            max_heap = []

            for num in arr:
                # Push a tuple (-distance, -value) so that the heap acts as a max-heap
                heapq.heappush(max_heap, (-abs(num - x), -num))

                # Keep only k elements in heap
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

            # Extract elements from heap and sort them
            result = sorted([-num for _, num in max_heap])
            return result

print(Solution().findClosestElements([1,2,3,4,5], 4, 3))  # Output: [1,2,3,4]