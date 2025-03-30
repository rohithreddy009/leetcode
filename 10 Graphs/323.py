from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        hmap = defaultdict(list)
        res = 0
        visit_set = set()

        for n1, n2 in edges:
            hmap[n1].append(n2)
            hmap[n2].append(n1)
        
        def dfs(node):
            visit_set.add(node)
            for neighbor in hmap[node]:
                if neighbor not in visit_set:
                    dfs(neighbor)
        
        for node in range(n):  # Iterate over all nodes, including isolated ones
            if node not in visit_set:
                res += 1  # Found a new component
                dfs(node)  # Explore the entire component
        
        return res

a = Solution()
print(a.countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2