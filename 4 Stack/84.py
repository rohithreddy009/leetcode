from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index, height
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res

a = Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))
