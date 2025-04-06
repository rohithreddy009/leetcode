from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        seen = set()

        for c, p in prerequisites:
            prereqs[c].append(p)
        
        def dfs(course):
            if course in seen:
                return True
            seen.add(course)
            for p in prereqs[course]:
                if dfs(p):
                    return True
            prereqs[course] = []
            seen.remove(course)
            return False

        for course in range(numCourses):
            if dfs(course):
                return False
        return True

a = Solution()     
print(a.canFinish(4, [[0,2], [2,1], [0,1], [3,0]])) # True
# print(a.canFinish(3, [[1,0],[2,1],[0,2],[2,0]])) # False