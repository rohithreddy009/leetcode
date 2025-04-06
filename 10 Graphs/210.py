from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = defaultdict(list)
        visit_set = set()
        seen_set = set()
        res = []

        for c, p in prerequisites:
            hmap[c].append(p)
        
        def dfs(course):
            if course in visit_set:
                return True
            if course in seen_set:
                return False
            else:
                visit_set.add(course)
                for p in hmap[course]:
                    if dfs(p):
                        return True
                visit_set.remove(course)
                seen_set.add(course)
                res.append(course)
                hmap[course] = []
                return False

        for course in range(numCourses):
            if dfs(course):
                return []
        return res

a = Solution()
print(a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,1,2,3]