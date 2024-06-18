# class Solution:
#     def topKFrequent(self, nums, k):
#         freq_map = {}
#         for num in nums:
#             if num in freq_map:
#                 freq_map[num] += 1
#             freq_map[num] = 1
#             sorted_elements = sorted(freq_map, key = lambda x: freq_map[x], reverse = True)
#         return sorted_elements[:k]

class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    

solution = Solution()

print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))


