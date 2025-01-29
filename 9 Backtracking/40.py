from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comb2(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return 
            
            # include candidates[i]
            curr.append(candidates[i])
            comb2(i+1, curr, total + candidates[i])
            curr.pop()

            # skip candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            comb2(i+1, curr, total)
        
        comb2(0,[],0)
        return res

Solution.combinationSum2(Solution(), [2,5,2,1,2], 5)