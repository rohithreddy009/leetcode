from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hmap = {}

        def dfs(node):
            if node in hmap:
                return hmap[node]
            
            copy = Node(node.val)
            hmap[node] = copy
            
            copy.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return copy
        
        return dfs(node)

