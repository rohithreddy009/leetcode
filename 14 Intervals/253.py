from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]  # Min-heap of end times
        meeting_rooms = 1

        for start, end in intervals[1:]:
            # If the room is free, remove the earliest ending meeting
            if start >= heap[0]:
                heapq.heappop(heap)

            # Add the current meeting's end time to the heap
            else:
                heapq.heappush(heap, end)
                meeting_rooms = max(meeting_rooms, len(heap))

        return meeting_rooms


print(Solution().minMeetingRooms([[0,30],[5,10],[15,20],[0,15],[21,25]]))  # 2
print(Solution().minMeetingRooms(intervals = [[7, 10], [2, 4]]))  # 1
print(Solution().minMeetingRooms(intervals = [[0, 30], [5, 10], [15, 20]]))  # 2