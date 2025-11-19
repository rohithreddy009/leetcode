from typing import Optional, List
import collections
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_col, max_col = 0, 0
        hmap = collections.defaultdict(list)
        q = deque([(root, 0)])
        res = []

        while q:
            node, col_val = q.popleft()
            min_col = min(min_col, col_val)
            max_col = max(max_col, col_val)
            hmap[col_val].append(node.val)

            if node.left:
                q.append((node.left, col_val - 1))
            if node.right:
                q.append((node.right, col_val + 1))
            
        for level in range(min_col, max_col + 1):
            res.append(hmap[level])
        return res