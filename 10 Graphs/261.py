from typing import List
from collections import defaultdict

class Solution: 
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        visit_set = set()
        hmap = defaultdict(list)

        for n1, n2 in edges:
            hmap[n1].append(n2)
            hmap[n2].append(n1)
        
        def dfs(i, prev):
            if i in visit_set:
                return False
            
            visit_set.add(i)
            for j in hmap[i]:
                if j == prev:
                    continue
                if dfs(j, i) == False:
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit_set)

a = Solution()
print(a.validTree(5, [[0,1], [0,2], [0,3], [1,4]])) # True
# print(a.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]])) # False    



        