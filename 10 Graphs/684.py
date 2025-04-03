from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        graph = defaultdict(set)
        
        def has_cycle(u, v, visited):
            if u in visited:
                return False
            if u == v:
                return True
            visited.add(u)
            for neighbor in graph[u]:
                if has_cycle(neighbor, v, visited):
                    return True
            return False
        
        for u, v in edges:
            if u in graph and v in graph and has_cycle(u, v, set()):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)
        
        return []

a = Solution()
print(a.findRedundantConnection([[1,2],[1,3],[2,3]]))  # Output: [2, 3]
# print(a.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # Output: [1, 4]