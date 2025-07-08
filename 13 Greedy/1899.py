from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res_set = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i in range(len(t)):
                if t[i] == target[i]:
                    res_set.add(i)
        
        return True if len(res_set) == 3 else False

print(Solution().mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))  # True
print(Solution().mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))  # False