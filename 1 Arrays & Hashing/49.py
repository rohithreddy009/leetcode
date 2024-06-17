from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # anagrams = {}
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if sorted_s not in anagrams:
        #         anagrams[sorted_s] = []
        #     anagrams[sorted_s].append(s)
        # return list(anagrams.values())

        anagrams = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams[key].append(s)
        return anagrams.values()


solution = Solution()

print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))