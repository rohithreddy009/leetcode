from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        res = []
        visited = set()
        seen = set()

        for c, p in prerequisites:
            prereqs[c].append(p)

        def dfs(course):
            if course in seen:
                return False
            if course in visited:
                return True
            
            seen.add(course)
            for p in prereqs[course]:
                if dfs(p) == False:
                    return False
            seen.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res

a = Solution()
print(a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,1,2,3]