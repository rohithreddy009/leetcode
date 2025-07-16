from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for start, end in intervals[1: ]:
            last_index = res[-1][1]

            if last_index >= start:
                res[-1][1] = max(last_index, end)
            else:
                res.append([start, end])
        
        return res

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]