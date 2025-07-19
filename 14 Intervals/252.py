from typing import List

class Solution:
    def canAttendmeetings(self, intervals: List[List[int]]) -> bool:    
        intervals.sort()
        cur_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < cur_end:
                return False
            cur_end = end
        return True



class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution2:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            for i in range(1, len(intervals)):
                if i1.end > i2.start:
                    return False
            return True
        

print(Solution().canAttendmeetings([[0,30],[5,10],[15,20]]))  # False
