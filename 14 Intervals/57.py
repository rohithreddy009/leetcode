from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # Case 1: newInterval is completely before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: newInterval is completely after current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Overlapping intervals, merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        # If newInterval was not added yet
        res.append(newInterval)
        return res

print(Solution().insert([[10,20],[30, 40],[50, 60]], [15, 55]))  
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) 