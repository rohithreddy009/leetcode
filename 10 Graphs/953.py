from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True
    
a = Solution()
print(a.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
print(a.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # False
print(a.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # False
print(a.isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz")) # True