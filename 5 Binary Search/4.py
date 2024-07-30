from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays into one sorted array
        merged = []
        i, j = 0, 0
        
        # Merge arrays while there are elements in both
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements from nums1 if any
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2 if any
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        # Find the median
        n = len(merged)
        if n % 2 == 1:
            # If odd, return the middle element
            return float(merged[n // 2])
        else:
            # If even, return the average of the two middle elements
            return (merged[(n - 1) // 2] + merged[n // 2]) / 2

solution = Solution()

# Define the test cases
nums1 = [1, 3]
nums2 = [10,20,33,44,66,90]
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

