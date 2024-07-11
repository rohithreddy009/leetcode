# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n1 = len(s1)
#         n2 = len(s2)

#         if n1 > n2:
#             return False

#         count_s1 = [0] * 26
#         count_s2 = [0] * 26

#         for i in range(len(s1)):
#             count_s1[ ord(s1[i]) - ord('a')] += 1
#             count_s2[ ord(s2[i]) - ord('a')] += 1

#         if count_s1 == count_s2:
#             return True

#         for i in range(len(s1), len(s2)):
#             count_s2[ ord(s2[i]) - ord('a')] += 1
#             count_s2[ ord(s2[i - n1]) - ord('a')] -= 1

#             if count_s1 == count_s2:
#                 return True
#         return False


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = Counter(s1)
        s2Count = Counter()

        len_s1 = len(s1)
        len_s2 = len(s2)

        for i in range(len_s2):
            # Add one more letter on the right side of the window
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

            # Remove one letter from the left side of the window
            if i >= len_s1:
                if s2Count[s2[i - len_s1]] == 1:
                    s2Count[s2[i - len_s1]] -= 1
                else:
                    s2Count[s2[i - len_s1]] -= 1

            # Compare the hashmap in the sliding window with the target hashmap
            if s1Count == s2Count:
                return True
        return False

a = Solution()
print(a.checkInclusion("ab","eidbaooo"))