from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        stack = ["JFK"]
        res = []

        for src, dst in sorted(tickets, reverse = True):
            graph[src].append(dst)
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        
        return reversed(res)

a = Solution()
# print(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))        
print(a.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
        