from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}

        for i, v in enumerate(s):
            hmap[v] = i
        
        res = []
        size, end = 0, 0
        
        for i, v in enumerate(s):
            size += 1
            if hmap[v] > end:
                end = hmap[v]
            if i == end:
                res.append(size)
                size = 0
        return res

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]